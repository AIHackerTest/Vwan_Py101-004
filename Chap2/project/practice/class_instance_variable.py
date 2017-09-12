class Test(object):
    id = 10
    def __init__(self,id):
        self.id = id

    def test_instance_method(self):
        return self.id

    @classmethod
    def test_class_method(self):
        return self.id

    @staticmethod
    def test_static_method():
        return Test.id

if __name__ == '__main__':
    te1 = Test(1)
    te2 = Test(2)
    print(f"instance id: {te1.id}")
    print(f"class id: {Test.id}")

    print('instance method call from instance 1:',te1.test_instance_method())
    print('instance method call from instance 2:',te2.test_instance_method())
    #print('instance method call from class:',Test.test_instance_method()) # should fail

    print('class method call from instance 1:',te1.test_class_method())
    print('class method call from instance 2:',te2.test_class_method())
    print('class method call from class:',Test.test_class_method())

    print('static method call from instance 1:',te1.test_static_method())
    print('static method call from instance 2:',te2.test_static_method())
    print('static method call from class:',Test.test_static_method())
