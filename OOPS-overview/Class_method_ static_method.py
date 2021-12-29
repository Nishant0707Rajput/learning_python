class ClassTest:

    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called a static method.")


an_instance_or_object = ClassTest()
an_instance_or_object.instance_method()
ClassTest.instance_method(an_instance_or_object)

print()

ClassTest.class_method()

print()

ClassTest.static_method()