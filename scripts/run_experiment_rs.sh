#!/bin/bash

STORM_HOME=/home/feature/storm/apache-storm-0.9.5/bin/storm

for workers in 2 4
do
for ackers in 2 4
do
for spouts in 1 10
do
for max_spout in 1 1000
do
for topology_level in 2 5 
do
for netty_min_wait in 10 1000
do
for message_size in 10 1000000
do
for buffer_size in 512 1024
do
for topology_serialized in "false" "true"
do
for priority in 0 29 
do
for bolts in 1 10
do

bin/stormbench -storm ${STORM_HOME} -jar ./target/storm-benchmark-0.1.0-jar-with-dependencies.jar -conf ./conf/rollingsort.yaml -c nimbus.host="localhost" -c topology.workers=$workers -c topology.transfer.buffer.size=$buffer_size -c topology.serialized.message.size.metrics=$topology_serialized -c topology.acker.executors=$ackers -c component.spout_num=$spouts -c topology.priority=$priority -c component.bolt_num=$bolts -c message.size=$message_size -c storm.messaging.netty.min_wait_ms=$netty_min_wait -c storm.messaging.netty.max_wait_ms=$(($netty_min_wait*10)) -c topology.max.spout.pending=$max_spout -c topology.level=$topology_level -c topology.builtin.metrics.bucket.size.secs=1 -c task.refresh.poll.secs=1 -c metrics.poll=10000 -c metrics.time=180000 storm.benchmark.tools.Runner storm.benchmark.benchmarks.RollingSort

${STORM_HOME} kill RollingSort

sleep 60

done
done
done
done
done
done
done
done
done
done
done
