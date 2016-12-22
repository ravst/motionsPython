from message_pb2 import *
import os
from subprocess import *
from pathlib2 import Path

binary = "/Users/ravst/motions/motions/.stack-work/dist/x86_64-osx/Cabal-1.22.5.0/build/motions/motions"

args = "-o {output} -n {name} -d {description} -s {steps} -x {callbacks} -f {frames}"

def make_string(s):
    return "\"s\""


def motions(inputData, output="/tmp/tmp", name="Simulation", description="Just a simulation", steps="1000", callbacks="[]", frames="100"):
    prepared_args = args.format(output=output, name=make_string(name), description=make_string(description), steps=steps, callbacks=callbacks, frames=frames).split(" ")
    #prepared_command = "/Users/ravst/motions/motions/.stack-work/dist/x86_64-osx/Cabal-1.22.5.0/build/motions/motions"
    inputBytes = inputData.SerializeToString()
    print prepared_args
    proc = Popen([binary] + prepared_args, stdin=PIPE, stdout=PIPE)
    outputBytes, _ = proc.communicate(input=inputBytes)
    message = SimulationState()
    message.ParseFromString(outputBytes)
    return message


#message = SimulationState()
#wejscie = Path("/Users/ravst/singleFrame.bytes").read_bytes()
#message.ParseFromString(wejscie)
#print str(motions(message))
