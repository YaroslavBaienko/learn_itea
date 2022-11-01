# class Phone:
#     number = '111-111-11'
#
#     def print_number(self):
#         print(f'Phone number: {self.number}')
#
#
# print(Phone.number)
#
# phone = Phone()
# Phone.print_number(phone)
#
# print(phone.number)
# phone.print_number()

class Phone:
    username = 'Bob'
    __how_many_times_turned_on = 0
    __serial_number = 'FA-124'

    def call(self):
        self.__how_many_times_turned_on += 1
        print(f'Ring-ring')

    def print_call_statistics(self):
        print(f'Times was turned on: {self.__how_many_times_turned_on}')

    def print_serial_number(self):
        print(f'Serial number: {self.__serial_number}')


phone = Phone()
phone.call()
phone.call()
phone.call()
phone.print_call_statistics()
phone._Phone__how_many_times_turned_on = 100
phone.print_call_statistics()
phone.print_serial_number()

# print(phone.username)
# print(phone._Phone__how_many_times_turned_on)

