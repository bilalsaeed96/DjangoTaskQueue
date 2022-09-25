import unittest
import requests
import json
import random


class DjangoTaskQueueTests(unittest.TestCase):

    def test_get_task_details(self):
        create_task = requests.post('http://nginx/api/tasks', {'object_id': random.randint(0, 100)})
        post_resp = create_task.json()
        
        get_request = requests.get(f'http://nginx/api/tasks/{post_resp.get("job_id")}')
        get_resp = get_request.json()
        
        self.assertEqual(get_resp.get('job_id'), post_resp.get('job_id'))
        self.assertEqual(get_request.status_code, 200)
    
    def test_create_new_job(self):
        object_id = random.randint(0, 100)
        create_task = requests.post('http://nginx/api/tasks', {'object_id': object_id})
        post_resp = create_task.json()
        
        self.assertEqual(post_resp.get('object_id'), object_id)
        self.assertEqual(create_task.status_code, 201)
    
    def test_get_task_details_invalid_id(self):
        get_request = requests.get(f'http://nginx/api/tasks/0')
        self.assertEqual(get_request.status_code, 404)


if __name__ == '__main__':
    unittest.main()
