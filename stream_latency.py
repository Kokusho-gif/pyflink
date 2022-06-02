from pyflink.common import Time, WatermarkStrategy, Duration
from pyflink.common.typeinfo import Types
from pyflink.common.types import Row
from pyflink.common.serialization import Encoder
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext, MapFunction
from pyflink.datastream.state import ValueStateDescriptor, StateTtlConfig
from pyflink.datastream.connectors import FileSource, StreamFormat, FileSink, OutputFileConfig, RollingPolicy
import time

class MyMapFunction(MapFunction):

    def map(self, value):
        line = value.split(",")

        return tuple(line)

def event_timer_timer_demo():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    ds = env.read_text_file(
        "/mnt/c/work/pyflink_demo/vir_linux/input.csv"
    ).map(MyMapFunction(), output_type=Types.TUPLE([Types.STRING(),Types.STRING(),Types.STRING()]))
    ds.print()



    beg_time = time.time()
    # submit for execution
    env.execute()
    print("PyFlink UDF consume time: " + str(time.time() - beg_time))


if __name__ == '__main__':
    event_timer_timer_demo()