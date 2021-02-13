from collections.abc import Iterable


class Cell:

   
    def __init__(self,init_value):
        self.__alternatives  = {i for i in range(1,10) if i!= init_value}                     #  задаем список возможных вариантов, цифры от 1 до 9 за исключением init_value  
        self.__value = init_value                                                             # задаем текущее значение клетки
        
 
    def exclude(self,exclude_digitals):                                  #исключение цифр из аргумента из множества возможных вариантов
        if  isinstance(exclude_digitals, Iterable):
            exclude_set = set(exclude_digitals)
        elif  isinstance(exclude_digitals, int):
            exclude_set = {exclude_digitals}
        else: raise ValueError('Incorrect value')    
        self.__alternatives.difference_update(exclude_set)                                                           

        
    @property
    def is_solved(self):
        if len(self.__alternatives) == 0: 
            return True
        else: return False


    @property
    def value(self):
        return self.__value


    @value.setter
    def value(self,new_value):
        if new_value in self.__alternatives:                                     # если аргумент есть в писке возможных вариантов
            if self.__value != None:                                             # если текущее значение не None
                self.__alternatives.add(self.__value)                            # текущее значение добавляем в список возможных вариантов 
            self.__alternatives.remove(new_value)                                # исключаем новое значение клетки из списка возможных вариантов
            self.__value = new_value                                             # меняем текущее значение клетки на новое 
        else: raise ValueError('Incorrect value')
        