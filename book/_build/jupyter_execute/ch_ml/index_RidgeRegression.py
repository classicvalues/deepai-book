#!/usr/bin/env python
# coding: utf-8

# # 2.2. Hồi qui Ridge và Lasso
# 
# Mục tiêu của bài viết này là giúp chúng ta hiểu về mô hình hồi qui `Ridge` và mô hình hồi qui `Lasso`. Giả định bạn đang xây dựng mô hình hồi qui tuyến tính nhưng thật không may mắn, mô hình của bạn gặp hiện tượng _quá khớp_ (_overfitting_). Khi đó bạn có thể nghĩ đến một số ý tưởng:
# 
# * Giảm bớt số lượng biến đầu vào.
# * Loại bỏ outliers.
# * Xử lý các trường hợp dữ liệu bị khuyết.
# * Thu thập thêm dữ liệu huấn luyện.
# * Thay đổi lớp mô hình.
# 
# ...
# 
# Có khá nhiều ý tưởng cho bạn thử nghiệm, một trong số chúng có thể giúp bạn khắc phục hiện tượng _quá khớp_. Đa phần các kĩ thuật đều liệu quan tới xử lý dữ liệu đầu vào một cách thủ công và cần phải cân nhắc trước khi đưa ra một quyết định thay đổi dữ liệu đầu vào.
# 
# Nhưng có một phương pháp khá hiệu quả giúp khắc phục tức thời hiện tượng _quá khớp_ mà không đòi hỏi chúng ta phải thay đổi dữ liệu. Đó chính là hồi qui _Ridge_ và _Lasso_ mà chúng ta sẽ tìm hiểu trong bài viết này.
# 
# Vậy thì _Ridge_ và _Lasso_ là những mô hình như thế nào? Vì sao chúng lại khắc phục được hiện tượng _quá khớp_?
# 
# Một cách khách quan, _Ridge_ và _Lasso_ là những biến thể của _hồi qui tuyến tính_ mà ở đó chúng ta thay đổi hàm _mất mát_ MSE để kiểm soát độ lớn của tham số huấn luyện nhằm giảm thiểu hiện tượng _quá khớp_ trong các bài toán dự báo của học có giám sát. Qua bài viết này bạn sẽ được tìm hiểu:
# 
# * Lý thuyết đằng sau hai lớp mô hình là gì?
# * Lời giải cho bài toán tối ưu.
# * Đặc điểm của nghiệm trả về.
# * Cách lựa chọn _hệ số điều chuẩn_ $\alpha$ phù hợp cho những mô hình này.
# 
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# RidgeRegression.md
# ```
