import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print('Start set_name test\n')
        for user in self.user_name:
            self.user_id.append(self.user_name.index(user))
            self.assertEqual(self.students.set_name(user),self.user_name.index(user))
            print(f"{self.user_name.index(user)} {user}")
        print("\nFinish set_name test\n\n")
    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print('Start get_name test\n')
        print(f'user_id length = {len(self.user_id)}')
        print(f'user_name length = {len(self.user_name)}\n')

        missing = sorted(set(range(min(self.user_id),max(self.user_id)+1))-set(sorted(self.user_id)))
        mex = missing[0] if missing else max(self.user_id) + 1
        for id in self.user_id:
            self.assertEqual(self.students.get_name(id),self.user_name[id])
            print(f'id {id} : {self.user_name[id]}')
        self.assertEqual(self.students.get_name(mex),"There is no such user")
        print(f'id {mex} : {self.students.get_name(mex)}')
        print("\nFinish get_name test")
      