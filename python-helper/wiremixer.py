#!/usr/bin/python
import sys
from WiremixerNode import WiremixerNode

# arguments <operation> [options]

#TODO: fill this with pipewire command and required parameters
def addNode(nodeName):
    print (f'add node {nodeName}')

#TODO:fill this with pipewire command and required parameters
def deleteNode(nodeName):
    print (f'delete node {nodeName}')

#TODO:fill this with pipewire command and required parameters
def linkNodes(firstNode, secondNode):
    print(f'linking {firstNode} with {secondNode}')

if(len(sys.argv)) <= 1:
    print('this should print help')
else:
    match sys.argv[1]:
        #test - only used as shortcut for testing small methods
        case 'test':
            node = WiremixerNode(sys.argv[2], sys.argv[3], sys.argv[4])
            print(node.getCommandString())
        case '-a' | 'add':
            if(len(sys.argv)) < 3:
                print('not enough arguments')
            else:
                addNode(sys.argv[2])
        case '-d' | 'delete':
            if(len(sys.argv)) < 3:
                print('not enough arguments')
            else:
                deleteNode(sys.argv[2])
        case '-l' | 'link':
            if(len(sys.argv)) < 4:
                print('not enough arguments')
            else:
                linkNodes(sys.argv[2], sys.argv[3])
        case _:
            print('nothing matched')

