# pomDependencyGenerator

An utility script to iterate over jars in a directory and generates related pom entries.   
Helpful if you are migrating from ant to Maven. 

**Note: ** Works with MavenCentral only.

## How it works??
1. Script iterates on directory passed as command-line argument. 
2. For each jar file :
  * First tries to query **"Maven central"** with **sha1 checksum** of the jar file.
  * If fails to identify with sha1, it switches to artifact & version search.
      * For each combination from jar name (Combinations using separator '-')
        * Query **"Maven central"** with **artifactName** and **version**.
        * On success returns result
  * If search is successful hit (found exact match) from either of the above methods, writes "dependency" markup entry at input directory.
  * If search is unsuccessful (happens 1/10 jars) writes a "dependency" mark-up entry with artifactId as Jar name.

## Usage:  
~~~~
python pomDependencyGenerator.py "< Absolute path to directory where your jar files are >"
~~~~
### Example:
Directory Listing : 
~~~~
commons-codec-1.7.jar
commons-collections-3.2.1.jar
commons-configuration-1.6.jar
commons-lang-2.4.jar
commons-logging-1.1.1.jar
guava-12.0.1.jar
hadoop-0.20.2-dev-core.jar
hadoop-auth-2.4.1.jar
hadoop-common-2.4.1.jar
hadoop-yarn-api-2.4.1.jar
hadoop-yarn-client-2.4.1.jar
hadoop-yarn-common-2.4.1.jar
hbase-0.94.21-mapr-1409.jar
hbase.client.api.jar
hbase.common.jar
htrace-core-2.04.jar
jackson-core-asl-1.8.8.jar
jackson-mapper-asl-1.8.8.jar
log4j-1.2.17.jar
maprfs-4.0.1-mapr.jar
netty-3.6.6.Final.jar
protobuf-java-2.5.0.jar
slf4j-api-1.6.4.jar
slf4j-log4j12-1.6.4.jar
zookeeper-3.4.5-mapr-1406.jar
~~~~

#### Output of the Script:
~~~~
Processed Jar Count: 25

Success : 19
Failed : 6
Found info for commons-codec-1.7.jar
Found info for commons-collections-3.2.1.jar
Found info for commons-configuration-1.6.jar
Found info for commons-lang-2.4.jar
Found info for commons-logging-1.1.1.jar
Found info for guava-12.0.1.jar
Found info for hadoop-auth-2.4.1.jar
Found info for hadoop-common-2.4.1.jar
Found info for hadoop-yarn-api-2.4.1.jar
Found info for hadoop-yarn-client-2.4.1.jar
Found info for hadoop-yarn-common-2.4.1.jar
Found info for htrace-core-2.04.jar
Found info for jackson-core-asl-1.8.8.jar
Found info for jackson-mapper-asl-1.8.8.jar
Found info for log4j-1.2.17.jar
Found info for netty-3.6.6.Final.jar
Found info for protobuf-java-2.5.0.jar
Found info for slf4j-api-1.6.4.jar
Found info for slf4j-log4j12-1.6.4.jar
No info found for hadoop-0.20.2-dev-core.jar
No info found for hbase-0.94.21-mapr-1409.jar
No info found for hbase.client.api.jar
No info found for hbase.common.jar
No info found for maprfs-4.0.1-mapr.jar
No info found for zookeeper-3.4.5-mapr-1406.jar
~~~~

Generated xml file post execution:  
```xml
<dependency>
	<groupId>commons-codec</groupId>
	<artifactId>commons-codec</artifactId>
	<version>1.7</version>
</dependency>
<dependency>
	<groupId>commons-collections</groupId>
	<artifactId>commons-collections</artifactId>
	<version>3.2.1</version>
</dependency>
<dependency>
	<groupId>commons-configuration</groupId>
	<artifactId>commons-configuration</artifactId>
	<version>1.6</version>
</dependency>
<dependency>
	<groupId>commons-lang</groupId>
	<artifactId>commons-lang</artifactId>
	<version>2.4</version>
</dependency>
<dependency>
	<groupId>commons-logging</groupId>
	<artifactId>commons-logging</artifactId>
	<version>1.1.1</version>
</dependency>
<dependency>
	<groupId>com.google.guava</groupId>
	<artifactId>guava</artifactId>
	<version>12.0.1</version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>hadoop-0.20.2-dev-core.jar</artifactId>
	<version></version>
</dependency>
<dependency>
	<groupId>org.apache.hadoop</groupId>
	<artifactId>hadoop-auth</artifactId>
	<version>2.4.1</version>
</dependency>
<dependency>
	<groupId>org.apache.hadoop</groupId>
	<artifactId>hadoop-common</artifactId>
	<version>2.4.1</version>
</dependency>
<dependency>
	<groupId>org.apache.hadoop</groupId>
	<artifactId>hadoop-yarn-api</artifactId>
	<version>2.4.1</version>
</dependency>
<dependency>
	<groupId>org.apache.hadoop</groupId>
	<artifactId>hadoop-yarn-client</artifactId>
	<version>2.4.1</version>
</dependency>
<dependency>
	<groupId>org.apache.hadoop</groupId>
	<artifactId>hadoop-yarn-common</artifactId>
	<version>2.4.1</version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>hbase-0.94.21-mapr-1409.jar</artifactId>
	<version></version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>hbase.client.api.jar</artifactId>
	<version></version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>hbase.common.jar</artifactId>
	<version></version>
</dependency>
<dependency>
	<groupId>org.cloudera.htrace</groupId>
	<artifactId>htrace-core</artifactId>
	<version>2.04</version>
</dependency>
<dependency>
	<groupId>org.codehaus.jackson</groupId>
	<artifactId>jackson-core-asl</artifactId>
	<version>1.8.8</version>
</dependency>
<dependency>
	<groupId>org.codehaus.jackson</groupId>
	<artifactId>jackson-mapper-asl</artifactId>
	<version>1.8.8</version>
</dependency>
<dependency>
	<groupId>log4j</groupId>
	<artifactId>log4j</artifactId>
	<version>1.2.17</version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>maprfs-4.0.1-mapr.jar</artifactId>
	<version></version>
</dependency>
<dependency>
	<groupId>io.netty</groupId>
	<artifactId>netty</artifactId>
	<version>3.6.6.Final</version>
</dependency>
<dependency>
	<groupId>com.google.protobuf</groupId>
	<artifactId>protobuf-java</artifactId>
	<version>2.5.0</version>
</dependency>
<dependency>
	<groupId>org.slf4j</groupId>
	<artifactId>slf4j-api</artifactId>
	<version>1.6.4</version>
</dependency>
<dependency>
	<groupId>org.slf4j</groupId>
	<artifactId>slf4j-log4j12</artifactId>
	<version>1.6.4</version>
</dependency>
<!-- TODO Find information on this jar file--->
<dependency>
	<groupId></groupId>
	<artifactId>zookeeper-3.4.5-mapr-1406.jar</artifactId>
	<version></version>
</dependency>

```


**Credits:** This script is an improved version of [Karl Tryggvason](http://stackoverflow.com/users/916371/karl-tryggvason)'s code on StackOverflow [Post](http://stackoverflow.com/a/23766172/639107).  
