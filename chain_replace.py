
def chain_replace(initial_string, replacement_list):
        """ recursive call to replace multiple things in a string - credit christian hogan """
        if not replacement_list:
            return initial_string

        replacement = replacement_list.pop(0)
        new_string = initial_string.replace(*replacement)

        return chain_replace(new_string, replacement_list)
        
      
def chain_replace_v2(initial_string, replacement_list):
        if not replacement_list:
            return initial_string
        return chain_replace( initial_string.replace(*replacement_list.pop(0)), replacement_list)
