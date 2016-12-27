#!/usr/bin/env python
import os
import sys
from subprocess import check_output

import requests


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[36m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[31m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def searchByShaChecksum(sha):
  searchurl = 'http://search.maven.org/solrsearch/select?q=1:%22' + sha + '%22&rows=20&wt=json'
  resp = requests.get(searchurl)
  data = resp.json()
  return data


def searchAsArtifact(artifact, version):
  searchurl = 'http://search.maven.org/solrsearch/select?q=a:"' + artifact + '" AND v:"' + version.strip() + '"&rows=20&wt=json'
  resp = requests.get(searchurl)
  # print(searchurl)
  data = resp.json()
  return data


def processAsArtifact(file: str):
  data = {'response': {'start': 0, 'docs': [], 'numFound': 0}}
  jar = file.replace(".jar", "")
  splits = jar.split("-")
  if (len(splits) < 2):
    return data
  for i in range(1, len(splits)):
    artifact = "-".join(splits[0:i])
    version = "-".join(splits[i:])
    data = searchAsArtifact(artifact, version)
    if data["response"] and data["response"]["numFound"] == 1:
      return data
  return data


def writeToPom(pom: object, grp: str = None, art: str = None, ver: str = None):
  if grp is not None and ver is not None:
    pom.write('<dependency>\n')
  else:
    pom.write('<!-- TODO Find information on this jar file--->\n')
    pom.write('<dependency>\n')
  grp = grp if grp is not None else ""
  art = art if art is not None else ""
  ver = ver if ver is not None else ""
  pom.write('\t<groupId>' + grp + '</groupId>\n')
  pom.write('\t<artifactId>' + art + '</artifactId>\n')
  pom.write('\t<version>' + ver + '</version>\n')
  pom.write('</dependency>\n')


def main(argv):
  if len(argv) == 0:
    print(bcolors.FAIL + 'Syntax : findPomJars.py <lib_dir_path>' + bcolors.ENDC)
  lib_home = str(argv[0])
  if os.path.exists(lib_home):
    os.chdir(lib_home)

    pom = open('./auto_gen_pom_list.xml', 'w')
    successList = []
    failedList = []
    jarCount = 0
    for lib in sorted(os.listdir(lib_home)):
      if lib.endswith(".jar"):
        jarCount += 1
        sys.stdout.write("\rProcessed Jar Count: %d" % jarCount)
        sys.stdout.flush()
        checkSum = check_output(["sha1sum", lib]).decode()
        sha = checkSum.split("  ")[0]
        jar = checkSum.split("  ")[1].strip()
        data = searchByShaChecksum(sha)
        if data["response"] and data["response"]["numFound"] == 0:
          data = processAsArtifact(jar)

        if data["response"] and data["response"]["numFound"] == 1:
          successList.append("Found info for " + jar)
          jarinfo = data["response"]["docs"][0]
          writeToPom(pom, jarinfo["g"], jarinfo["a"], jarinfo["v"])
        else:
          failedList.append("No info found for " + jar)
          writeToPom(pom, art=jar.replace(".jar\n", ""))
    pom.close()

    print("\n")
    print("Success : %d" % len(successList))
    print("Failed : %d" % len(failedList))

    for entry in successList:
      print(entry)
    for entry in failedList:
      print(entry)

  else:
    print
    bcolors.FAIL + lib_home, " directory doesn't exists" + bcolors.ENDC


if __name__ == "__main__":
  main(sys.argv[1:])
