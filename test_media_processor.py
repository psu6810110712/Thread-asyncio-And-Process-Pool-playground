import unittest
import asyncio
from unittest.mock import patch
import media_processor

class TestMediaProcessor(unittest.TestCase):
    
    # 1. Arrange: กำหนด MEDIA_LIST จำลองสำหรับใช้ในการทดสอบ
    # เราจำลองข้อมูลที่เล็กลงเพื่อให้เทสต์รันได้อย่างรวดเร็ว
    MOCK_MEDIA_LIST = ["Test Movie 1", "Test Movie 2", "Test Movie 3"]

    @patch('media_processor.MEDIA_LIST', MOCK_MEDIA_LIST)
    def test_run_asyncio(self):
        # 2. Act: รันฟังก์ชัน Concurrency ที่ต้องการทดสอบ
        results = asyncio.run(media_processor.run_asyncio())
        
        # 3. Assert: เช็คว่าจำนวนผลลัพธ์ที่ได้ครบถ้วนตาม List หรือไม่
        self.assertEqual(len(results), len(self.MOCK_MEDIA_LIST))
        # ตรวจสอบความถูกต้องของข้อความในผลลัพธ์
        for res in results:
            self.assertIn("Async:", res)

    @patch('media_processor.MEDIA_LIST', MOCK_MEDIA_LIST)
    def test_run_threading(self):
        # 2. Act
        results = media_processor.run_threading()
        
        # 3. Assert
        self.assertEqual(len(results), len(self.MOCK_MEDIA_LIST))
        for res in results:
            self.assertIn("Thread:", res)

    @patch('media_processor.MEDIA_LIST', MOCK_MEDIA_LIST)
    def test_run_multiprocessing(self):
        # 2. Act
        results = media_processor.run_multiprocessing()
        
        # 3. Assert
        self.assertEqual(len(results), len(self.MOCK_MEDIA_LIST))
        for res in results:
            self.assertIn("Process:", res)

if __name__ == '__main__':
    unittest.main()
