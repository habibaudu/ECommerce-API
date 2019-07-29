import json
from ECommerceAPI.tests.base_config import BaseConfiguration


class DepartmentTestcase(BaseConfiguration):

        def test_create_department(self):
            response = self.csrf_client.post('/api/v1/departments/',
                                             data=self.department,
                                             format='json',
                                             HTTP_AUTHORIZATION="Token "+self.user)
            self.assertEqual(response.status_code, 201)

        def test_create_department_with_invalid_data(self):
            data = self.department
            data["name"] = "reginol@@"
            response = self.csrf_client.post('/api/v1/departments/',
                                             data=data,
                                             format='json',
                                             HTTP_AUTHORIZATION="Token "+self.user)
            self.assertEqual(response.status_code, 400)

        def test_get_all_departments(self):
            response = self.csrf_client.get('/api/v1/departments/',
                                             HTTP_AUTHORIZATION="Token "+self.user)
            self.assertEqual(response.status_code, 200)

        def test_get_a_department(self):
            department = self.dept.id
            url = '/api/v1/department/'+str(department)+"/"
            response = self.csrf_client.get(url,
                                             HTTP_AUTHORIZATION="Token "+self.user)
            self.assertEqual(response.status_code, 200)
