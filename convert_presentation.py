def get_name(slide):
    for shape in slide.shapes:
      if shape.is_placeholder:
         if shape.placeholder_format.idx == 0:
             return shape.text
    return "" #Not an exception because this is the *name*, which isn't needed for OBZ
