# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root 
# for full license information.
# ==============================================================================

# This file is auto-generated by _fetch_ops.py.

from cntk.graph import ComputationNode, _InputComputationNodeBase, _ImageInputComputationNodeBase

class Slice(ComputationNode):
    def __init__(self, _, beginIndex, endIndex, axis=1, op_name='CNTK2.Slice',
            name=None):
        super(Slice, self).__init__(params=['_', 'beginIndex', 'endIndex', 'axis'], op_name=op_name, name=name)
        self._ = _
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.axis = axis
        self.inputs = ['_']
        self.params_with_defaults = ['axis']

class Ceil(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Ceil', name=None):
        super(Ceil, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.inputs = ['_']
        self.params_with_defaults = []

class ElementDivide(ComputationNode):
    def __init__(self, _, y,  op_name='CNTK2.ElementDivide', name=None):
        super(ElementDivide, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.inputs = ['_', 'y']
        self.params_with_defaults = []

class Round(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Round', name=None):
        super(Round, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.inputs = ['_']
        self.params_with_defaults = []

class DynamicAxis(ComputationNode):
    def __init__(self, op_name='CNTK2.DynamicAxis', name=None):
        super(DynamicAxis, self).__init__(params=[], op_name=op_name, name=name)

        self.params_with_defaults = []
        self.inputs = []

class Input(_InputComputationNodeBase):
    def __init__(self, shape, dynamicAxis='', tag='feature', op_name='CNTK2.Input', name=None):
        super(Input, self).__init__(params=['shape', 'dynamicAxis', 'tag'], op_name=op_name, name=name)
        self.shape = shape
        self.dynamicAxis = dynamicAxis
        self.tag = tag
        self.params_with_defaults = ['dynamicAxis', 'tag']
        self.inputs = []

class _Parameter(ComputationNode):
    def __init__(self, shape, value=0, learningRateMultiplier=1.0, init='uniform', initValueScale=1, initFromFilePath='', initFromLiteral='', initOnCPUOnly=True, randomSeed=-1, op_name='CNTK2._Parameter', name=None):
        super(_Parameter, self).__init__(params=['shape', 'value', 'learningRateMultiplier', 'init', 'initValueScale', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed'], op_name=op_name, name=name)
        self.shape = shape
        self.value = value
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.initFromFilePath = initFromFilePath
        self.initFromLiteral = initFromLiteral
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed
        self.params_with_defaults = ['value', 'learningRateMultiplier', 'init', 'initValueScale', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed']
        self.inputs = []

class Reshape(ComputationNode):
    def __init__(self, _, shape, beginAxis=0, endAxis=0, op_name='CNTK2.Reshape', name=None):
        super(Reshape, self).__init__(params=['_', 'shape', 'beginAxis', 'endAxis'], op_name=op_name, name=name)
        self._ = _
        self.shape = shape
        self.beginAxis = beginAxis
        self.endAxis = endAxis
        self.params_with_defaults = ['beginAxis', 'endAxis']
        self.inputs = ['_']

class Times(ComputationNode):
    def __init__(self, x, y, outputRank=1, op_name='CNTK2.Times', name=None):
        super(Times, self).__init__(params=['x', 'y', 'outputRank'], op_name=op_name, name=name)
        self.x = x
        self.y = y
        self.outputRank = outputRank
        self.params_with_defaults = ['outputRank']
        self.inputs = ['x', 'y']

class Abs(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Abs', name=None):
        super(Abs, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class Clip(ComputationNode):
    def __init__(self, _, minValue, maxValue, op_name='CNTK2.Clip', name=None):
        super(Clip, self).__init__(params=['_', 'minValue', 'maxValue'], op_name=op_name, name=name)
        self._ = _
        self.minValue = minValue
        self.maxValue = maxValue
        self.params_with_defaults = []
        self.inputs = ['minValue', 'maxValue', '_']

class ElementTimes(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.ElementTimes', name=None):
        super(ElementTimes, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Floor(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Floor', name=None):
        super(Floor, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class Minus(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.Minus', name=None):
        super(Minus, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Plus(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.Plus', name=None):
        super(Plus, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Less(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.Less', name=None):
        super(Less, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Equal(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.Equal', name=None):
        super(Equal, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Greater(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.Greater', name=None):
        super(Greater, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class GreaterEqual(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.GreaterEqual', name=None):
        super(GreaterEqual, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class NotEqual(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.NotEqual', name=None):
        super(NotEqual, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class LessEqual(ComputationNode):
    def __init__(self, _, y, op_name='CNTK2.LessEqual', name=None):
        super(LessEqual, self).__init__(params=['_', 'y'], op_name=op_name, name=name)
        self._ = _
        self.y = y
        self.params_with_defaults = []
        self.inputs = ['_', 'y']

class Tanh(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Tanh', name=None):
        super(Tanh, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class FutureValue(ComputationNode):
    def __init__(self, _, shape, timeStep=1, defaultHiddenActivation=0.1, op_name='CNTK2.FutureValue', name=None):
        super(FutureValue, self).__init__(params=['_', 'shape', 'timeStep', 'defaultHiddenActivation'], op_name=op_name, name=name)
        self._ = _
        self.shape = shape
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']
        self.inputs = ['_']

class PastValue(ComputationNode):
    def __init__(self, _, shape, timeStep=1, defaultHiddenActivation=0.1, op_name='CNTK2.PastValue', name=None):
        super(PastValue, self).__init__(params=['_', 'shape', 'timeStep', 'defaultHiddenActivation'], op_name=op_name, name=name)
        self._ = _
        self.shape = shape
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']
        self.inputs = ['_']

class Relu(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Relu', name=None):
        super(Relu, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class Sigmoid(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Sigmoid', name=None):
        super(Sigmoid, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class Softmax(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Softmax', name=None):
        super(Softmax, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class CrossEntropyWithSoftmax(ComputationNode):
    def __init__(self, _, outProbVectorSequence, op_name='CNTK2.CrossEntropyWithSoftmax', name=None):
        super(CrossEntropyWithSoftmax, self).__init__(params=['_', 'outProbVectorSequence'], op_name=op_name, name=name)
        self._ = _
        self.outProbVectorSequence = outProbVectorSequence
        self.params_with_defaults = []
        self.inputs = ['_', 'outProbVectorSequence']

class ErrorPrediction(ComputationNode):
    def __init__(self, _, outVectorSequence, op_name='CNTK2.ErrorPrediction', name=None):
        super(ErrorPrediction, self).__init__(params=['_', 'outVectorSequence'], op_name=op_name, name=name)
        self._ = _
        self.outVectorSequence = outVectorSequence
        self.params_with_defaults = []
        self.inputs = ['_', 'outVectorSequence']

class Log(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Log', name=None):
        super(Log, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']

class Exp(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Exp', name=None):
        super(Exp, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']
        
class Sqrt(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Sqrt', name=None):
        super(Sqrt, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']        
        
class Square(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Square', name=None):
        super(Square, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']                

class Pass(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Pass', name=None):
        super(Pass, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']     

class Dropout(ComputationNode):
    def __init__(self, _, op_name='CNTK2.Dropout', name=None):
        super(Dropout, self).__init__(params=['_'], op_name=op_name, name=name)
        self._ = _
        self.params_with_defaults = []
        self.inputs = ['_']
        
class TransposeDimensions(ComputationNode):
    def __init__(self, _, axis1, axis2, op_name='CNTK2.TransposeDimensions', name=None):
        super(TransposeDimensions, self).__init__(params=['_', 'axis1', 'axis2'], op_name=op_name, name=name)
        self._ = _
        self.axis1 = axis1
        self.axis2 = axis2
        self.params_with_defaults = []
        self.inputs = ['_']        
