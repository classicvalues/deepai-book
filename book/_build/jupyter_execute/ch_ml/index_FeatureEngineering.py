#!/usr/bin/env python
# coding: utf-8

# Thuật ngữ:
# 
# * Feature Extraction: Trích lọc đặc trưng
# * Feature Transformation: Biến đổi đặc trưng
# * Feature Selection: Lựa chọn đặc trưng
# * Bag of words: Phương pháp túi từ
# * Standardization: Phương pháp chuẩn hoá

# # 11. Giới thiệu về feature engineering

# Nếu như mô hình học máy là cỗ máy sản xuất thì dữ liệu được ví như nguyên liệu và kết quả dự báo là sản phẩm. Một trong những cách để cải thiện sản phẩm đó là chuẩn bị nguyên liệu tốt. Thông qua _Feature Engineering_ chúng ta có thể tạo ra những đặc trưng đầu vào tốt giúp huấn luyện mô hình phân loại hoặc dự báo với độ chính xác cao, sai số thấp. Chính vì vậy các kĩ thuật _Feature Engineering_ đóng một vai trò rất quan trọng khi xây dựng và huấn luyện mô hình. Cùng theo dõi một số người nổi tiếng đã nói về tầm quan trọng của Feature Engineering:
# 
# "Feature engineering is the art part of data science."
# > _Sergey Yurgenson, former #1 ranked global competitive data scientist on Kaggle_
# 
# Tức là _Feature Engineering_ là một phần nghệ thuật của khoa học dữ liệu.
# 
# "Coming up with features is difficult, time-consuming, [and] requires expert knowledge." 
# 
# > _Andrew Ng, chief scientist of Baidu, co-chairman and co-founder of Coursera, and adjunct professor at Stanford University_
# 
# Tạm dịch: Nghĩ ra đặc trưng rất khó, tiêu tốn nhiều thời gian và đòi hỏi hiểu biết chuyên môn.
# 
# Đối với các lớp mô hình _Deep Learning_ thì quá trình _Feature Engineering_ được thực hiện tự động thông qua một kiến trúc _end-to-end_. Trong khi các mô hình _Machine Learning_ truyền thống thì chúng ta phải tạo lập đặc trưng bằng những phương pháp thủ công.
# 
# Qua bài viết này chúng ta cùng tìm hiều thêm các phương pháp chính trong _Feature Engineering_ bao gồm:
# 
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# FeatureEngineering.md
# ```
