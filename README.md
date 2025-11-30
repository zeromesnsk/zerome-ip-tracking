# IP Tracking

  
  #    একটি শক্তিশালী 
IP ম্যানেজমেন্ট এবং সিকিউরিটি টুল।


<p align="center">
  <img src="Screenshot_20250911_140024.jpg" alt="Screenshot" width="600" style="border-radius:15px; box-shadow:0 4px 12px rgba(0,0,0,0.3);" />
</p>

## বৈশিষ্ট্যসমূহ
- IP অ্যাড্রেস তথ্য দেখুন
- IP ব্লক/আনব্লক করুন
- IP স্ক্যান করুন
- IP ট্র্যাক করুন

## ইন্সটলেশন

Termux-এ ইন্সটল করতে:

```bash
pkg update && pkg upgrade
pkg install python
rm -rf ip-tracking
git clone https://github.com/zeromesnsk/ip-tracking.git
cd ip-tracking
pip install -r requirements.txt
python main.py
