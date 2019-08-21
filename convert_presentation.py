from pptx import Presentation

def get_name(slide):
    for shape in slide.shapes:
      if shape.is_placeholder:
         if shape.placeholder_format.idx == 0:
             return shape.text
    return "" #Not an exception because this is the *name*, which isn't needed for OBZ


def is_first_inside_second(first,second):
    "Finds the centre the first shape and checks if it is in the bounds of the second"
    y=first['top']+(first['height']/2)-second['top']
    x=first['left']+(first['width']/2)-second['left']
    if 0 < y < second['height']:
        if 0 < x <second['width']:
            return True 
    return False


def hollow_shape(temp):
    hollow_shape={}
    hollow_shape['top']=temp.top
    hollow_shape['left']=temp.left
    hollow_shape['height']=temp.height
    hollow_shape['width']=temp.width
    return hollow_shape
    


def get_containers(slide):
    comparisions=0
    is_container={}
    hollow_shapes=[]
    for i in range(len(slide.shapes)):
        hollow_shapes.append(hollow_shape(slide.shapes[i]))
    is_container[0]=True #the one closest to the back is a container. 
    for shape_num in range(len(slide.shapes)):
        potential_container=True
        for container_num in is_container.keys():
            comparisions+=1
            if is_first_inside_second(hollow_shapes[shape_num],hollow_shapes[container_num]): 
                potential_container=False
                break
        if potential_container:
            is_container[shape_num]=True 
    containers=[] 
    for shape_num in is_container.keys():
            containers.append(slide.shapes[shape_num])
    print "total comparisons {}".format(comparisions)
    return containers
