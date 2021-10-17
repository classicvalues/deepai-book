#!/usr/bin/env python
# coding: utf-8

# # 1. Đại số tuyến tính
# 
# ## 1.1. Số vô hướng (scalar)
# 
# Trong cuộc sống hàng ngày chúng ta sẽ gặp rất nhiều số vô hướng (scalar). Giá trị của tiền nhà tháng này mà bạn phải trả cho chủ nhà là một số vô hướng. Bạn vừa thực hiện một bài kiểm tra toán, bạn được 9 điểm thì điểm số này là một số vô hướng,.... Tóm lại số vô hướng là một con số cụ thể. Số vô hướng sẽ khác với biến số vì biến số có thể nhận nhiều giá trị trong khi số vô hướng chỉ nhận một giá trị duy nhất. Ví dụ, khi biểu diễn giá nhà $y$ theo diện tích $x$ theo phương trình $y=20x + 200$ thì các số  vô hướng là $20, 200$ và các biến là $x, y$.
# 
# Để khởi tạo một số vô hướng, chúng ta sẽ sử dụng tensor
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# a = torch.tensor(20)
# b = torch.tensor(200)
# print("diện tích x = 50 --> giá nhà y = a*50+b = ", a*50+b)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# a = np.array(20)
# b = np.array(200)
# print("diện tích x = 50 --> giá nhà y = a*50+b = ", a*50+b)
# :::
# ::::
# 
# Số vô hướng có thể được coi như hằng số trong một phương trình. Chúng ta có thể thực hiện các phép toán cộng/trừ/nhân/chia với số vô hướng như với hằng số.
# 
# ## 1.2. Véc tơ
# 
# Véc tơ là một khái niệm cơ bản nhất của toán học. Chúng ta có thể coi véc tơ là một tập hợp nhiều giá trị của số vô hướng. Véc tơ thường biểu diễn một đại lượng cụ thể trên thực tiễn. Ví dụ như diện tích của các căn nhà là một véc tơ, số lượng phòng ngủ cũng là một véc tơ. Véc tơ có độ dài đặc trưng chính bằng số lượng các phần tử trong nó. Để khởi tạo một véc tơ, trong pytorch chúng ta bao các giá trị của nó trong dấu ngoặc vuông.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# x = torch.tensor([1, 1.2, 1.5, 1.8, 2])
# x
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# x = np.array([1, 1.2, 1.5, 1.8, 2])
# x
# ::::
# 
# ### 1.2.1. Các thuộc tính của véc tơ
# 
# Một véc tơ sẽ có độ dài và định dạng dữ liệu xác định. Ngoài ra nếu coi một biến số là một véc tơ thì trong thống kê mô tả chúng ta sẽ quan tâm tới tổng, trung bình, phương sai, giá trị lớn nhất, nhỏ nhất.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Độ dài
# print("length of vector: ", x.size()) # or len(x)
# 
# # Định dạng của véc tơ
# print("vector type: ", x.dtype)
# 
# # Tổng của các phần tử 
# print("sum of vector: ", x.sum())
# 
# # Trung bình các phần tử
# print("mean of vector: ", x.mean())
# 
# # Giá trị nhỏ nhất
# print("min of vector: ", x.min())
# 
# # Giá trị lớn nhất
# print("max of vector: ", x.max())
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Độ dài
# print("length of vector: ", x.shape) # or len(x)
# 
# # Định dạng của véc tơ
# print("vector type: ", x.dtype)
# 
# # Tổng của các phần tử 
# print("sum of vector: ", x.sum())
# 
# # Trung bình các phần tử
# print("mean of vector: ", x.mean())
# 
# # Giá trị nhỏ nhất
# print("min of vector: ", x.min())
# 
# # Giá trị lớn nhất
# print("max of vector: ", x.max())
# :::
# ::::
# 
# ### 1.2.2. Các phép tính trên véc tơ
# 
# Chúng ta có thể thực hiện các phép tính trên véc tơ như phép cộng, trừ, tích vô hướng, tích có hướng giữa hai véc tơ.. Lưu ý là chúng phải có cùng độ dài. Trong khuôn khổ cuốn sách này, các véc tơ sẽ được ký hiệu là một ký tự chữ thường in đậm như $\mathbf{x}, \mathbf{y}, \mathbf{z}$. Ngoài ra $\mathbf{x}\in \mathbb{R}^{n}$ là véc tơ số thực có độ dài $n$.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# x = torch.tensor([1, 2, 1.5, 1.8, 1.9])
# y = torch.tensor([1.1, 2.2, 1.2, 1.6, 1.7])
# print("x + y: ", x + y)
# print("x - y: ", x - y)
# print("x * y: ", x * y)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# x = np.array([1, 2, 1.5, 1.8, 1.9])
# y = np.array([1.1, 2.2, 1.2, 1.6, 1.7])
# print("x + y: ", x + y)
# print("x - y: ", x - y)
# print("x * y: ", x * y)
# :::
# ::::
# 
# Véc tơ có thể thực hiện các phép cộng, trừ, nhân, chia với một số vô hướng. Giá trị thu được là một véc tơ cùng kích thước mà mỗi phần tử của nó là kết quả được thực hiện trên từng phần tử của véc tơ với số vô hướng đó.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# x = torch.tensor([1, 2, 1.5, 1.8, 1.9])
# print("x + 5: ", x + 5)
# print("x - 5: ", x - 5)
# print("x * 5: ", x * 5)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# x = np.array([1, 2, 1.5, 1.8, 1.9])
# print("x + 5: ", x + 5)
# print("x - 5: ", x - 5)
# print("x * 5: ", x * 5)
# :::
# ::::
# 
# 
# ## 1.3. Ma trận
# 
# Véc tơ là đại lượng một chiều nên nó chỉ có thể biểu diễn cho một biến. Trong trường hợp chúng ta cần biểu diễn cho nhiều biến thì sẽ cần tới đại lượng hai chiều là ma trận. Ma trận được ký hiệu bởi một chữ cái in đậm $\mathbf{A} \in \mathbb{R}^{m\times n}$ là một ma trận số thực có $m$ dòng và $n$ cột.
# 
# $$\begin{split}\mathbf{A}=\begin{bmatrix} 
# a_{11} & a_{12} & \cdots & a_{1n} \\ 
# a_{21} & a_{22} & \cdots & a_{2n} \\ 
# \vdots & \vdots & \ddots & \vdots \\ 
# a_{m1} & a_{m2} & \cdots & a_{mn} \\ 
# \end{bmatrix}.\end{split}$$
# 
# Để xác định một phần tử bất kỳ thuộc dòng thứ $i$, cột thứ $j$ của ma trận $\mathbf{A}$ ta ký hiệu chúng là $\mathbf{A}_{ij}$. Véc tơ dòng thứ $i$ sẽ là $\mathbf{A}_{i:}$ và véc tơ cột thứ $j$ sẽ là $\mathbf{A}_{:j}$. Để đơn giản hoá ta qui ước $\mathbf{A}_{j}$ là véc tơ cột $j$ và $\mathbf{A}^{(i)}$ là véc tơ dòng $i$.
# 
# ### 1.3.1. Các ma trận đặc biệt
# 
# * Ma trận vuông: Ma trận vuông là ma trận có số dòng bằng số cột. Ma trận vuông rất quan trọng vì khi tìm nghiệm cho hệ phương trình, từ ma trận vuông ta có thể chuyển sang ma trận tam giác. Ma trận vuông cũng là ma trận có thể tính được giá trị định thức. Tóm lại ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ vuông nếu $m=n$. 
# 
# * Ma trận đơn vị: Là ma trận có đường chéo chính bằng 1, các phần tử còn lại bằng $0$. Ví dụ ma trận đơn vị kích thước $3 \times 3$ được ký hiệu là $\mathbf{I}_3$ có gía trị là:
# 
# $$\begin{split}\mathbf{I}_3=
# \begin{bmatrix} 
# 1 & 0 & 0 \\ 
# 0 & 1 & 0 \\ 
# 0 & 0 & 1 
# \end{bmatrix}
# \end{split}$$
# 
# Tóm lại, $\mathbf{A}$ là ma trận đơn vị nếu nó là ma trận vuông và $a_{ij} = 1$ nếu $i=j$ và $a_{ij} = 0$ nếu $i \neq j$.
# 
# * Ma trận đường chéo: Là ma trận có các phần tử trên đường chéo chính khác 0 và các phần tử còn lại bằng 0. Ví dụ về ma trận đường chéo:
# 
# 
# $$\begin{split}\mathbf{A}=
# \begin{bmatrix} 
# 1 & 0 & 0 \\ 
# 0 & 2 & 0 \\ 
# 0 & 0 & 3 
# \end{bmatrix}
# \end{split}$$
# 
# 
# * Ma trận chuyển vị: $\mathbf{B}$ là ma trận chuyển vị của $\mathbf{A}$ nếu $b_{ij} = a_{ji}$ với mọi $i, j$. Dễ hiểu hơn, tức là mọi dòng của ma trận $A$ sẽ là cột của ma trận $\mathbf{B}$. Ví dụ:
# 
# $$\begin{split}\mathbf{A}=
# \begin{bmatrix} 
# 1 & 2 & 3 \\ 
# 3 & 2 & 1
# \end{bmatrix}
# \end{split}, \begin{split}\mathbf{B}=
# \begin{bmatrix} 
# 1 & 3 \\
# 2 & 2 \\ 
# 3 & 1\end{bmatrix}
# \end{split}$$
# 
# 
# Ký hiệu chuyển vị của ma trận $\mathbf{A}$ là $\mathbf{A}^{\intercal}$
# 
# ### 1.3.2. Các thuộc tính của ma trận
# 
# Một ma trận được đặc trưng bởi dòng và cột.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# A = torch.tensor([[1, 2, 3], 
#                   [3, 2, 1]])
# 
# # shape của matrix A
# A.size()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# A = np.array([[1, 2, 3], 
#               [3, 2, 1]])
# 
# # shape của matrix A
# A.shape
# :::
# ::::
# 
# ### 1.3.3. Các phép tính trên ma trận
# 
# Hai ma trận có cùng kích thước chúng ta có thể thực hiện các phép cộng, trừ, tích hadamard (hoặc elementi-wise). Ma trận thu được cũng có cùng kích thước và các phần tử của nó được tính dựa trên các phần tử có cùng vị trí trên cả hai ma trận $\mathbf{A}$ và $\mathbf{B}$.
# 
# **Tích hadamard hoặc element-wise**
# 
# $$
# \begin{split}\mathbf{A} \odot \mathbf{B} =
# \begin{bmatrix}
#     a_{11}  b_{11} & a_{12}  b_{12} & \dots  & a_{1n}  b_{1n} \\
#     a_{21}  b_{21} & a_{22}  b_{22} & \dots  & a_{2n}  b_{2n} \\
#     \vdots & \vdots & \ddots & \vdots \\
#     a_{m1}  b_{m1} & a_{m2}  b_{m2} & \dots  & a_{mn}  b_{mn}
# \end{bmatrix}\end{split}
# $$
# 
# Trên pytorch chúng ta có thể tính tích hadamard của hai ma trận đơn giản như sau:
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# A = torch.tensor([[1, 2, 3], 
#                   [3, 2, 1]])
# 
# B = torch.tensor([[2, 1, 2], 
#                   [1, 3, 0]])
# 
# A*B
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# A = np.array([[1, 2, 3], 
#               [3, 2, 1]])
# 
# B = np.array([[2, 1, 2], 
#              [1, 3, 0]])
# 
# A*B
# :::
# ::::
# 
# Tương tự với các phép cộng và trừ
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# print("A-B: \n", A-B)
# print("A+B: \n", A+B)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# print("A-B: \n", A-B)
# print("A+B: \n", A+B)
# :::
# ::::
# 
# **Tích thông thường**: Tích thông thường giữa hai ma trận $\mathbf{A}$ có kích thước $m \times n$ và $\mathbf{B}$ có kích thước $n \times p$ là một ma trận có kích thước $m \times p$. Ma trận output $\mathbf{C}$ có giá trị tại phần tử $c_{ij} = \mathbf{A}^{(i)} \mathbf{B}_{j}$ (dòng thứ $i$ của ma trận $\mathbf{A}$ nhân với cột thứ $j$ của ma trận $\mathbf{B}$).
# 
# $$
# \begin{split}\mathbf{A}_{m \times n} \mathbf{B}_{n \times p} =
# \begin{bmatrix}
#     \mathbf{A}^{(1)}  \mathbf{B}_{1} & \mathbf{A}^{(1)}  \mathbf{B}_{2} & \dots  & \mathbf{A}^{(1)}  \mathbf{B}_{p} \\
#     \mathbf{A}^{(2)}  \mathbf{B}_{1} & \mathbf{A}^{(2)}  \mathbf{B}_{2} & \dots  & \mathbf{A}^{(2)}  \mathbf{B}_{p} \\
#     \vdots & \vdots & \ddots & \vdots \\
#     \mathbf{A}^{(m)}  \mathbf{B}_{1} & \mathbf{A}^{(m)}  \mathbf{B}_{2} & \dots  & \mathbf{A}^{(m)}  \mathbf{B}_{p} \\
# \end{bmatrix}\end{split}_{m \times p}
# $$
# 
# Chắc các bạn còn nhớ $\mathbf{A}^{(i)}$ là véc tơ dòng và $\mathbf{A}_{j}$ là véc tơ cột.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# A = torch.tensor([[1, 2, 3], 
#                   [3, 2, 1]])
# 
# B = torch.tensor([[2, 1], 
#                   [1, 3],
#                   [1, 1]])
# 
# A@B
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# A = np.array([[1, 2, 3], 
#               [3, 2, 1]])
# 
# B = np.array([[2, 1], 
#               [1, 3],
#               [1, 1]])
# 
# A@B
# :::
# ::::
# 
# ### 1.3.4. Ma trận nghịch đảo
# 
# Cho ma trận vuông $\mathbf{A} \in \mathbb{R}^{n \times n}$, nếu tồn tại một ma trận vuông $\mathbf{B} \in \mathbb{R}^{n \times n}$ sao cho $\mathbf{A} \mathbf{B} = \mathbf{I}_{n}$ thì ta nói rằng ma trận $\mathbf{A}$ _khả nghịch_ (_invertible_) hoăc _không suy biến_ (_nonsingular_). Ma trận $\mathbf{B}$ được gọi là _ma trận nghịch đảo_ (_inverse matrix_) của ma trận $\mathbf{A}$. Ta dễ dàng nhận thấy rằng nếu $\mathbf{A} \mathbf{B} = \mathbf{I}_n$ thì 
# 
# $$\begin{eqnarray}\det(\mathbf{A} \mathbf{B}) & = & \det(\mathbf{I}_n) \\
# \leftrightarrow \det(\mathbf{A}) \det(\mathbf{B}) & = & 1 \\
# \end{eqnarray}$$
# 
# Như vậy để ma trận $\mathbf{A}$ khả nghịch thì $\det(\mathbf{A}) \neq 0$. Trong trường hợp không tồn tại ma trận $\mathbf{B}$ thoả mãn điều kiện $\mathbf{A} \mathbf{B} = \mathbf{I}$ thì ta nói rằng ma trận $\mathbf{A}$ _không khả nghịch_ hoặc bị _suy biến_ (_singular_).
# 
# Ma trận nghịch đảo của _ma trận khả nghịch_ $\mathbf{A}$ được kí hiệu là $\mathbf{A}^{-1}$ là một ma trận vuông thoả mãn:
# 
# $$\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}_{n}$$
# 
# Ta dễ  nhận thấy rằng $\mathbf{A}^{-1} = \mathbf{B}$. Ma trận nghịch đảo thường được sử dụng để giải hệ phương trình tuyến tính. Giả sử một hệ phương trình tuyến tính:
# 
# $$\mathbf{A} \mathbf{x} = \mathbf{b} \tag{1}$$
# 
# Trong đó ma trận hệ số $\mathbf{A} \in \mathbb{R}^{n \times n}$ có các dòng tương ứng với các hệ số của một phương trình. Véc tơ $\mathbf{x} \in \mathbb{R}^{n}$ là biến cần tìm. Véc tơ $\mathbf{b}$ đại diện cho hệ số tự do. 
# 
# Khi đó để tìm nghiệm $\mathbf{x}$ chúng ta tính theo ma trận nghịch đảo $\mathbf{A}^{-1}$:
# 
# $$\begin{eqnarray}
# \mathbf{A} \mathbf{x} & = & \mathbf{b} \\
# \leftrightarrow \underbrace{\mathbf{A}^{-1} \mathbf{A}}_{\mathbf{I}}\mathbf{x} & = & \mathbf{A}^{-1}\mathbf{b} \\
# \mathbf{I}\mathbf{x} & = & \mathbf{A}^{-1}\mathbf{b} \\
# \mathbf{x} & = & \mathbf{A}^{-1}\mathbf{b}
# \end{eqnarray}$$
# 
# Một số tính chất liên quan tới ma trận nghịch đảo.
# 
# * Nếu ma trận $\mathbf{A}$ là một ma trận vuông nhưng không khả nghịch thì phương trình $(1)$ có vô số nghiệm. Trong trường hợp ma trận $\mathbf{A}$ không vuông và là một ma trận thấp chiều (có số dòng lớn hơn số cột) thì phương trình có thể vô nghiệm.
# 
# * Nếu ma trận $\mathbf{A}$ khả nghịch thì ma trận nghịch đảo của nó là $\mathbf{B}$ cũng khả nghịch. Đồng thời ta có tính chất:
# 
# $$\mathbf{A}^{-1} = \mathbf{B} ~ \text{and} ~ \mathbf{B}^{-1} = \mathbf{A}$$
# 
# **Chứng minh**:
# 
# Ta có:
# 
# $$\mathbf{A}\mathbf{B} = \mathbf{I} \tag{2}$$
# 
# Nhân $\mathbf{A}^{-1}$ vào bên trái mỗi vế của phương trình $(2)$ ta được:
# 
# $$\begin{eqnarray}
# \mathbf{A}\mathbf{B} & = & \mathbf{I} \\
# \underbrace{\mathbf{A}^{-1}\mathbf{A}}_{\mathbf{I}}\mathbf{B} & = & \underbrace{\mathbf{A}^{-1}\mathbf{I}}_{\mathbf{A}^{-1}} \\
# \mathbf{B} & = & \mathbf{A}^{-1}
# \end{eqnarray}$$
# 
# 
# * Nếu ma trận $\mathbf{A}, \mathbf{B}$ đều khả nghịch thì tích của chúng cũng khả nghịch:
# 
# $$(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$$
# 
# **chứng minh**:
# 
# Nhân mỗi vế của phương trình trên với $\mathbf{A}\mathbf{B}$ vào bên phải ta có:
# 
# Đối với vế bên trái:
# 
# $$(\mathbf{A}\mathbf{B})^{-1} (\mathbf{A}\mathbf{B}) = \mathbf{I}$$
# 
# Đối với vế bên phải:
# 
# $$(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{B}^{-1}\underbrace{(\mathbf{A}^{-1}\mathbf{A})}_{\mathbf{I}}\mathbf{B} = \underbrace{\mathbf{B}^{-1}\mathbf{I}}_{\mathbf{B}^{-1}}\mathbf{B} = \mathbf{B}^{-1}\mathbf{B} = \mathbf{I}$$
# 
# Từ đó suy ra $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
# 
# Trên numpy để tính ma trận nghịch đảo chúng ta sử dụng hàm `np.linalg.pinv` hoặc `np.linalg.inv`. Hàm `np.linalg.pinv` sẽ bao gồm cả trường hợp $\mathbf{A}$ không khả nghịch, giá trị trả về là một ma trận giả nghịch đảo (_pseudo-inverse matrix_). 
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# A = torch.tensor([[1, 2, 3], 
#               [3, 2, 1],
#               [4, 2, 2]], dtype=torch.float32)
# 
# A_inv = torch.linalg.pinv(A)
# print(A_inv)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# A = np.array([[1, 2, 3], 
#               [3, 2, 1],
#               [4, 2, 2]])
# 
# A_inv = np.linalg.pinv(A)
# print(A_inv)
# :::
# ::::
# 
# 
# ### 1.3.5. Truy cập thành phần
# 
# Chúng ta có thể truy cập vào các thành phần của ma trận $\mathbf{A}$ dựa theo các chỉ số slice index. Chúng ta có thể tổng hợp kiến thức về truy cập thành phần trong bản sau:
# 
# | Cú pháp      | Mô tả |
# | ----------- | ----------- |
# | :n      | lấy n index đầu tiên từ [0, 1, ..., n-1]       |
# | -n:   | lấy n index cuối cùng từ [len-n, ..., len-1]        |
# | i:j   | lấy các index từ [i, i+1, ..., j-1]        |
# | ::2   | lấy các index chẵn liên tiếp [0, 2, 4 ..., int(len/2)*2]        |
# | ::k   | lấy các index cách đều và chia hết cho k một cách liên tiếp [0, k, 2k, ..., int(len/k)*k]        |
# | :   | lấy toàn bộ index        |
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# A = torch.tensor([[1, 2, 3], 
#                   [3, 2, 1],
#                   [4, 2, 2]])
# 
# # Truy cập ma trận con từ 2 dòng đầu tiên và 2 cột đầu tiên.
# A[:2, :2]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# A = np.array([[1, 2, 3], 
#               [3, 2, 1],
#               [4, 2, 2]])
# 
# # Truy cập ma trận con từ 2 dòng đầu tiên và 2 cột đầu tiên.
# A[:2, :2]
# :::
# ::::
# 
# Truy cập ma trận con từ 2 dòng cuối cùng và 2 cột đầu tiên
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập ma trận con từ 2 dòng cuối cùng và 2 cột đầu tiên
# A[-2:, :2]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập ma trận con từ 2 dòng cuối cùng và 2 cột đầu tiên
# A[-2:, :2]
# :::
# ::::
# 
# Truy cập véc tơ con từ dòng thứ 2 và 2 cột cuối cùng.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập véc tơ con từ dòng thứ 2 và 2 cột cuối cùng.
# print(A[2, -2:])
# 
# # Hoặc
# A[2:3, -2:][0]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập véc tơ con từ dòng thứ 2 và 2 cột cuối cùng.
# print(A[2, -2:])
# 
# # Hoặc
# A[2:3, -2:][0]
# :::
# ::::
# 
# Truy cập ma trận có các dòng chẵn
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập ma trận có các dòng chẵn
# A[::2, :]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập ma trận có các dòng chẵn
# A[::2, :]
# :::
# ::::
# 
# Truy cập một index cụ thể, ví dụ dòng 0, 2 của ma trận
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập một index cụ thể , ví dụ dòng 0, 2 của ma trận
# A.index_select(0, torch.tensor([0, 2]))
# # Trong công thức trên 0 là chiều mà ta sẽ lấy, tensor([0, 2]) là các index ta sẽ lấy từ chiều 0.
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập một index cụ thể , ví dụ dòng 0, 2 của ma trận
# A[[0, 2], :]
# :::
# ::::
# 
# ## 1.4. Tensor
# 
# Tensor là một định dạng đặc biệt được sáng tạo ra bởi google. Nó tổng quát hơn so với ma trận vì có thể biểu diễn được các không gian với số chiều tuỳ ý. Chẳng hạn trong xử lý ảnh chúng ta có một bức ảnh với kích thước là $W \times H \times C$ lần lượt $W, H, C$ là chiều _width, height và channels_. Thông thường $C = 1$ hoặc $3$ tuỳ theo ảnh là ảnh xám hay ảnh màu RGB. Trong huấn luyện mô hình phân loại ảnh thì các đầu vào được kết hợp theo mini-batch nên sẽ có thêm một chiều về batch_size. Do đó input có kích thước là $N \times W \times H \times C$.
# 
# ### 1.4.1. Các thuộc tính của tensor
# 
# Một tensor được đặc trưng bởi kích thước các chiều, số lượng chiều, định dạng dữ liệu của tensor.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# A = torch.tensor([[[1, 2, 3], 
#                   [3, 2, 1]],
#                   [[2, 1, 2], 
#                   [1, 3, 0]]])
# 
# # Kích thước của tensor
# print("shape of A: " , A.size())
# 
# # Số chiều 
# print("total dim: ", A.ndim)
# 
# # Định dạng dữ liệu
# print("dtype: ", A.dtype)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# A = np.array([[[1, 2, 3], 
#               [3, 2, 1]],
#               [[2, 1, 2], 
#               [1, 3, 0]]])
# 
# # Kích thước của array
# print("shape of A: " , A.shape)
# 
# # Số chiều 
# print("total dim: ", A.ndim)
# 
# # Định dạng dữ liệu
# print("dtype: ", A.dtype)
# :::
# ::::
# 
# ### 1.4.2. Các phép tính trên tensor
# 
# **Tích thông thường giữa 2 tensors**: Nếu tensor $\mathbf{A}$ có kích thước $m \times n \times p$ và tensor $\mathbf{B}$ có kích thước $n \times p \times q$ thì tích giữa chúng có kích thước là $m \times n \times q$. Trên python chúng ta sử dụng ký hiệu `@` để đại diện cho tích thông thường.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# A = torch.randn([2, 3, 4])
# B = torch.randn([2, 4, 2])
# 
# # Tích giữa 2 tensor
# (A@B).size()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# A = np.random.randn(2, 3, 4)
# B = np.random.randn(2, 4, 2)
# 
# # Tích giữa 2 array
# (A@B).shape
# :::
# ::::
# 
# Ngoài ra chúng ta có thể tính **tích hadamard giữa 2 tensors** $\mathbf{A}$ và $\mathbf{B}$ được ký hiệu bằng dấu `*` như sau:
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# A = torch.randn([2, 3, 4])
# B = torch.randn([2, 3, 4])
# 
# # Tích hadamard giữa 2 tensor
# (A*B).size()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# A = np.random.randn(2, 3, 4)
# B = np.random.randn(2, 3, 4)
# 
# # Tích hadamard giữa 2 array
# (A*B).shape
# :::
# ::::
# 
# Chúng ta cũng có thể thực hiện các phép cộng, trừ giữa các tensor cùng kích thước.
# 
# Phép cộng
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Phép cộng
# (A+B).size()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Phép cộng
# (A+B).shape
# :::
# ::::
# 
# Phép trừ
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Phép trừ
# (A-B).size()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Phép trừ
# (A-B).shape
# :::
# ::::
# 
# **Truy cập thành phần**: Để truy cập vào một mảng thành phần của $\mathbf{A}$ chúng ta sẽ cần khai báo vị trí indices của chúng trên mỗi chiều của ma trận $\mathbf{A}$. Cách truy cập cũng hoàn toàn tương tự như đối với ma trận.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# # Khởi tạo ma trận A kích thước m, n, p = 2, 3, 4
# A = torch.randn([2, 3, 4])
# 
# # Truy cập ma trận đầu tiên 
# A[:1, :, :]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# # Khởi tạo ma trận A kích thước m, n, p = 2, 3, 4
# A = np.random.randn(2, 3, 4)
# 
# # Truy cập ma trận đầu tiên 
# A[:1, :, :]
# :::
# ::::
# 
# Truy cập ma trận đầu tiên và chỉ lấy dòng từ 1 tới 3
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập ma trận đầu tiên và chỉ lấy dòng từ 1 tới 3
# A[0][1:3, :]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập ma trận đầu tiên và chỉ lấy dòng từ 1 tới 3
# A[0][1:3, :]
# :::
# ::::
# 
# Truy cập tương ứng với các chiều m, n, p lần lượt index đầu tiên, 2 index đầu tiên, và index thứ 3.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # Truy cập tương ứng với các chiều m, n, p lần lượt index đầu tiên, 2 index đầu tiên, và index thứ 3.
# A[:1, :2, 3]
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # Truy cập tương ứng với các chiều m, n, p lần lượt index đầu tiên, 2 index đầu tiên, và index thứ 3.
# A[:1, :2, 3]
# :::
# ::::
# 
# ## 1.5. Tích giữa một ma trận với véc tơ
# 
# Bản chất của phép nhân một ma trận với một véc tơ là một **phép biến hình**. Giả sử bạn có ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ và véc tơ $\mathbf{x} \in \mathbb{R}^{n}$. Khi đó tích giữa ma trận $\mathbf{A}$ với véc tơ $\mathbf{x}$ là một véc tơ $\mathbf{y}$ trong không gian mới $\mathbf{y} \in \mathbb{R}^{m}$. $\mathbf{y}$ được xem như ảnh của $\mathbf{x}$ khi chiếu lên không gian $m$ chiều thông qua hàm ánh xạ $f(\mathbf{x}) = \mathbf{A}\mathbf{x}$.
# 
# $$\mathbf{A}\mathbf{x} =
# \begin{bmatrix}
# \mathbf{a}^\top_{1} \\
# \mathbf{a}^\top_{2} \\
# \vdots \\
# \mathbf{a}^\top_m \\
# \end{bmatrix} \mathbf{x} = \begin{bmatrix}
# \mathbf{a}^\top_{1} \mathbf{x} \\
# \mathbf{a}^\top_{2} \mathbf{x} \\
# \vdots \\
# \mathbf{a}^\top_m \mathbf{x} \\
# \end{bmatrix} = \begin{bmatrix}
# y_1 \\
# y_2 \\
# \vdots \\
# y_m
# \end{bmatrix} = \mathbf{y}$$
# 
# Như vậy thông qua ma trận $\mathbf{A}$ chúng ta đã biến đổi véc tơ $\mathbf{x}$ từ không gian $n$ chiều sang véc tơ $\mathbf{y}$ trong không gian $m$ chiều. Khi lựa chọn số chiều $m$ trong không gian mới nhỏ hơn, chúng ta thu được một đầu ra $\mathbf{y}$ là hình ảnh giảm chiều của véc tơ đầu vào $\mathbf{x}$. Phép biến đổi này thường xuyên được áp dụng trong machine learning để nhằm giảm chiều dữ liệu, đặc biệt là ở những layer fully connected cuối cùng của mạng nơ ron. Trong _phân tích suy biến_ (_singular decomposition_) chúng ta cũng sử dụng phép biến đổi không gian để tạo thành một véc tơ mới sao cho tích vô hướng giữa hai véc tơ bất kì được bảo toàn. Bạn sẽ được đọc thêm về phép phân tích suy biến ở những chương sau. Các phép xoay ảnh cũng biến đổi toạ độ các điểm sang không gian mới bằng cách nhân véc tơ toạ độ của chúng với ma trận xoay rotation.
# 
# Một ứng dụng đặc biệt quan trọng của phép nhân ma trận với một véc tơ là trong hồi qui tuyến tính. Để tính được giá trị dự báo của biến mục tiêu $\hat{y}$ chúng ta cần nhân ma trận đầu vào $\mathbf{X}$ với véc tơ hệ số ước lượng $\mathbf{w}$. Ví dụ, khi đã biết được các biến đầu vào gồm: diện tích và số phòng ngủ như các dòng của ma trận bên dưới:
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# X = torch.tensor([[100, 120, 80, 90, 105, 95], 
#                   [2, 3, 2, 2, 3, 2]])
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# X = np.array([[100, 120, 80, 90, 105, 95], 
#               [2, 3, 2, 2, 3, 2]])
# :::
# ::::
# 
# Và hệ số hồi qui tương ứng với với chúng lần lượt là $\mathbf{w} = (10, 100)$. Khi đó giá nhà có thể được ước lượng bằng tích $\mathbf{y} = \mathbf{X}^{\top}\mathbf{w}$
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# w = torch.tensor([[10], [100]])
# y = X.T@w
# y
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# w = np.array([[10], [100]])
# y = X.T@w
# y
# :::
# ::::
# 
# ## 1.6. Tích vô hướng (_inner product_)
# 
# Tích vô hướng giữa hai véc tơ $\mathbf{x}, \mathbf{y} \in \mathbb{R}^{d}$ có cùng kích thước là một số vô hướng được ký hiệu là $\langle \mathbf{x}, \mathbf{y} \rangle$ hoặc $\mathbf{x}^{\top}\mathbf{y}$ có công thức như sau:
# 
# $$\langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^{d} x_i y_i$$
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# x = torch.tensor([1, 2, 3])
# y = torch.tensor([2, 3, 4])
# x.dot(y)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# x = np.array([1, 2, 3])
# y = np.array([2, 3, 4])
# x.dot(y)
# :::
# ::::
# 
# Tích vô hướng rất quan trọng. Đây cũng là lý do mà tôi phải tách chúng thành một mục riêng. Bạn có thể bắt gặp tích vô hướng rất nhiều trong machine learning. Bên dưới là một số tình huống thường gặp:
# 
# - Tích vô hướng có thể được sử dụng để tính giá trị ước lượng của phương trình hồi qui tuyến tính. Ví dụ nếu bạn biết giá nhà được biểu diễn theo diện tích $x_1$ và số phòng ngủ $x_2$ theo công thức: 
# 
# $$y=20x_1 + 10x_2+ 200$$
# 
# Thì một cách khái quát bạn có thể ước lượng $y$ theo tích vô hướng giữa véc tơ đầu vào $\mathbf{x}^{\top} = (x_1, x_2, 1)$ và véc tơ hệ số $\mathbf{w} = (20, 10, 200)$ như sau:
#  
# $$\hat{y} = \mathbf{x}^{\top}\mathbf{w}$$
# 
# - Tích vô hướng cũng được sử dụng để tính trung bình có trọng số của $\mathbf{x}$:
# 
# $$\bar{\mathbf{x}} = \sum_{i=1}^{n} x_i q_i= \mathbf{x}^{\top}\mathbf{q}$$
# với $\sum_{i=1}^{n} q_i= 1$
# 
# - Ngoài ra, chắc hẳn bạn còn nhớ cách tính cos giữa hai véc tơ $\mathbf{x}$ và $\mathbf{y}$ sẽ bằng tích vô hướng giữa hai véc tơ được chuẩn hoá theo norm chuẩn bậc 2.
# 
# $$\cos({\mathbf{x}, \mathbf{y}}) = \frac{\sum_{i=1}^{d} x_i y_i}{ \sqrt{\sum_{i=1}^{d} x_i^2} \sqrt{\sum_{i=1}^d y_i^2}}= \frac{\langle \mathbf{x}, \mathbf{y} \rangle}{\mathbf{||x||_2}\mathbf{||y||_2}}
# $$
# 
# Khái niệm về norm chuẩn bậc 2 cũng là một kiến thức rất quan trọng. Mình sẽ giúp các bạn tìm hiểu bên dưới.
# 
# 
# ## 1.7. Khái niệm chuẩn
# 
# Chuẩn là một khái niệm liên quan đến véc tơ. Hay nói chính xác hơn nó là một độ đo trên véc tơ để so sánh các véc tơ với nhau. Cụ thể hơn: 
# 
# $f(\mathbf{x})$ là một phép ánh xạ từ véc tơ sang một đại lượng vô hướng $\mathbb{R}^{d} \mapsto \mathbb{R}$ nếu nó thoả mãn các tính chất.
# 
# 1-. Tính chất co dãn: 
# 
# $$\alpha f(\mathbf{x}) = f(\alpha\mathbf{x})$$
# 
# Như vậy khi bạn phóng đại lên véc tơ $\alpha$ lần thì giá trị chuẩn của nó cũng phóng đại lên $\alpha$ lần.
# 
# 2-. Bất đẳng thức tam giác: 
# 
# $$f(\mathbf{x} + \mathbf{y}) \leq f(\mathbf{x}) + f(
#   \mathbf{y}
# )$$
# 
# Nếu ta coi $\mathbf{x}$ như là véc tơ cạnh và $f(\mathbf{x})$ như là độ dài cạnh của một tam giác thì $f(\mathbf{x}), f(\mathbf{y})$ là độ dài của 2 cạnh bất kỳ và tổng của chúng sẽ lớn hơn độ dài cạnh còn lại $f(\mathbf{x} + \mathbf{y})$.
# 
# 3-. Tính chất không âm: 
# 
# $$f(\mathbf{x}) \geq 0, \forall \mathbf{x}$$
# 
# Tính chất này là hiển nhiên vì đã là độ đo thì không được âm.

# Trong machine learning các bạn sẽ thường xuyên gặp một số chuẩn chính là chuẩn bậc 2 
# 
# $$L_{2} = \|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2 }$$
# 
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# x = torch.randn(10)
# torch.norm(x, p=2)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# x = np.random.randn(10)
# np.linalg.norm(x, ord=2)
# :::
# ::::
# 
# Ta nhận thấy hàm MSE đo lường sai số giữa giá trị dự báo và thực tế trong phương trình hồi qui tuyến tính cũng là một dạng chuẩn bậc 2.
# 
# Chuẩn bậc 1:
# 
# $$L_{1} = \|\mathbf{x}\|_1 = \sum_{i=1}^n \left|x_i \right| $$
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# print(torch.norm(x, p=1))
# # hoặc 
# torch.abs(x).sum()
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# print(np.linalg.norm(x, ord=1))
# # hoặc 
# np.abs(x).sum()
# :::
# ::::
# 
# 
# Trong hồi qui tuyến tính thì chuẩn bậc 1 đo lường sai số tuyệt đối giữa giá trị dự báo và giá trị thực tế. Tuy nhiên nó ít được sử dụng hơn so với chuẩn bậc 2 như là một loss function vì giá trị của nó có đạo hàm không liên tục. Điều này dẫn tới việc huấn luyện mô hình không ổn định. Tuy nhiên nó cũng khá thường xuyên được sử dụng trong các mô hình deep learning chẳng hạn như GAN.
# 
# Cả hai chuẩn trên đều là trường hợp cụ thể của chuẩn bậc $p$ (ký hiệu $L_{p}$) tổng quát hơn có công thức như sau:
# 
# $$L_{p} = \|\mathbf{x}\|_p = \left(\sum_{i=1}^n \left|x_i \right|^p \right)^{1/p}$$
# 
# Để cả 3 điều kiện về chuẩn được thoả mãn thì chúng ta cần có $p \geq 1$.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# # chuẩn p bất kỳ >= 1, chẳng hạn p=1.5
# torch.norm(x, p=1.5)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# # chuẩn p bất kỳ >= 1, chẳng hạn p=1.5
# np.linalg.norm(x, ord=1.5)
# :::
# ::::
# 
# ## 1.8. Định thức và các tính chất của định thức
# 
# Giả sử ta có một ma trận vuông $\mathbf{A}$ như sau:
# 
# $$\mathbf{A}=\begin{bmatrix} 
# a_{11} & a_{12} & \dots & a_{1n} \\ 
# a_{21} & a_{22} & \dots & a_{2n} \\ 
# \dots & \dots & \ddots & \dots \\ 
# a_{n1} & a_{n2} & \dots & a_{nn} \\ 
# \end{bmatrix}$$
# 
# 
# Định thức của một ma trận $\mathbf{A}$ được kí hiệu là $| \mathbf{A} |$ hoặc $\det(\mathbf{A})$ là một giá trị được tính theo công thức:
# 
# $$\det(\mathbf{A})= \sum_{(\sigma_1, \sigma_2, \dots, \sigma_n) \in \mathcal{S}} \text{sgn}(\sigma) a_{1\sigma_1}a_{2\sigma_2}\cdots a_{n\sigma_n}$$
# 
# Trong đó $\sigma=(\sigma_1, \sigma_2, \dots, \sigma_n)$ là một phép hoán vị các thành phần của tập hợp $n$ số tự nhiên đầu tiên $O = \{1, 2, \dots, n\}$. Tập hợp tất cả các hoán vị của $n$ số tự nhiên này còn được kí hiệu là $\mathcal{S}$. Hàm $\text{sgn}(\sigma)$ là một hàm nhận hai gía trị $\{1, -1\}$. Nếu số lần hoán vị $\sigma$ để biến đổi trở về tập $O$ là chẵn thì nhận gía trị 1 và lẻ thì nhận giá trị -1.
# 
# Trong `numpy`, định thức có thể được tính toán khá dễ dàng thông qua hàm `np.linalg.det()`.
# 
# ::::{tabbed} pytorch
# :::{code-block} python
# import torch
# 
# A = torch.tensor([[1, 2],
#                   [3, 4]], dtype=torch.float32)
# 
# # Định thức của ma trận
# torch.det(A)
# :::
# ::::
# 
# ::::{tabbed} numpy
# :::{code-block} python
# import numpy as np
# 
# A = np.array([[1, 2],
#               [3, 4]])
# 
# # Định thức của ma trận
# np.linalg.det(A)
# :::
# ::::
# 
# Ngoài ra định thức của ma trận $\mathbf{A}$ có thể được khai triển theo các _ma trận phần bù_ $\mathbf{A}_{ij}$ của ma trận $\mathbf{A}$. Trong đó ma trận phần bù $\mathbf{A}_{ij}$ là ma trận được tạo thành bằng cách xoá đi dòng thứ $i$ và cột thứ $j$ của ma trận $\mathbf{A}$.
# 
# $$\det(\mathbf{A}) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \det(\mathbf{A}_{ij})$$
# 
# Định thức có vai trò rất quan trọng trong đại số tuyến tính. Thông qua định thức, chúng ta có thể biết được hệ các véc tơ dòng (hoặc cột) của một ma trận là độc lập tuyến tính hay phụ thuộc tuyến tính? Hệ phương trình tương ứng với ma trận có thể có bao nhiêu nghiệm? Bên dưới là một số tính chất của định thức:
# 
# 1-. Định thức chỉ tồn tại trên những ma trận vuông.
# 
# 2-. $\text{det}(\mathbf{A}) = \text{det}(\mathbf{A}^{\intercal})$
# 
# 3-. $\det(\mathbf{I}) = 1$
# 
# 4-. Một ma trận đường chéo thì có định thức bằng tích các phần tử nằm trên đường chéo. Ma trận đường chéo còn được kí hiệu thông qua các phần tử trên đường chéo là $\text{diag}(a_1, a_2, \dots, a_m)$. Tức là nếu:
# 
# $$\mathbf{A} = \text{diag}(a_1, a_2, \dots, a_m)=\begin{bmatrix} 
# a_{1} & 0 & \dots & 0\\ 
# 0 & a_{2} & \dots & 0\\ 
# \dots & \dots & \ddots & \dots\\ 
# 0 & 0 & \dots & a_{m}\\ 
# \end{bmatrix}$$
# 
# thì:
# 
# $$\text{det}(\mathbf{A}_{m \times m}) = a_1.a_2 \dots a_m$$
# 
# 
# 5-. Nếu $\mathbf{A}, \mathbf{B}$ là những ma trận vuông cùng kích thước thì 
# 
# $$\text{det}(\mathbf{AB}) = \text{det}(\mathbf{BA}) = \det({\mathbf{A}}) \det({\mathbf{B}})$$
# 
# Cũng từ tính chất này ta suy ra:
# 
# $$\det{(\mathbf{A} \mathbf{B} \mathbf{C})} = \det(\mathbf{A}) \det(\mathbf{B}) \det(\mathbf{C})$$
# 
# 6-. Ma trận vuông $\mathbf{A}$ khả nghịch thì 
# 
# $$\text{det}(\mathbf{A}) = \frac{1}{\text{det}{(\mathbf{A}^{-1})}}$$
# 
# Từ tính chất này ta cũng suy ra một ma trận khả nghịch thì định thức của nó phải khác 0 bởi nếu định thức của nó bằng 0 thì $\det(\mathbf{A}) = 0$, điều này là vô lý vì vế phải của phương trình trên không thể bằng 0.
# 
# 7-. Nếu một ma trận tồn tại một véc tơ dòng hoặc véc tơ cột có toàn bộ các phần tử bằng 0 thì định thức của ma trận bằng 0.
# 
# 8-. Trong một ma trận nếu đổi vị trí của hai dòng bất kì hoặc hai cột bất kì và các vị trí còn lại dữ nguyên thì định thức đổi dấu. Tức là nếu bên dưới ta có hai ma trận vuông:
# 
# $$\mathbf{A}=\begin{bmatrix} 
# \mathbf{A}_{1:} \\ 
# \dots \\ 
# \mathbf{A}_{i:} \\
# \dots \\ 
# \mathbf{A}_{j:} \\
# \dots \\ 
# \mathbf{A}_{n:} \\
# \end{bmatrix} ~ \text{and} ~ 
# \mathbf{A'}=\begin{bmatrix} 
# \mathbf{A}_{1:} \\ 
# \dots \\ 
# \mathbf{A}_{j:} \\
# \dots \\ 
# \mathbf{A}_{i:} \\
# \dots \\ 
# \mathbf{A}_{n:} \\
# \end{bmatrix}$$
# 
# Trong đó ma trận $\mathbf{A'}$ thu được bằng cách thay đổi vị trí dòng $\mathbf{A}_{i:}$ cho dòng $\mathbf{A}_{j:}$ của ma trận $\mathbf{A}$ thì $\det({\mathbf{A}}) = -\det(\mathbf{A'})$.
# 
# 9-. Khi cộng vào một dòng tích của một dòng khác với hệ số $\alpha$ hoặc cộng vào một cột với tích của một cột khác với hệ số $\alpha$ thì định thức không đổi. 
# 
# 10-. Khi nhân một dòng hoặc một cột bất kì của ma trận với hệ số $\alpha$ và các dòng và cột khác giữa nguyên thì định thức của ma trận mới tăng gấp $\alpha$ lần. Như vậy ta suy ra một tính chất khá quan trọng đối với ma trận $\mathbf{A} \in \mathbb{R}^{n \times n}$:
# 
# $$\det(\alpha \mathbf{A}) = \alpha^{n} \det(\mathbf{A})$$
# 
# ## 1.9. Tổ hợp tuyến tính và không gian sinh
# 
# **Thế nào là một tổ hợp tuyến tính?**
# 
# Giả sử $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n$ là các véc tơ thuộc không gian $\mathbb{R}^m$ và $k_1, k_2, \dots, k_n$ là những số vô hướng. Khi đó _tổ hợp tuyến tính_ (_linear combination_) của $n$ véc tơ $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n$ tương ứng với các hệ số $k_i$ là một véc tơ được tính theo phương trình tuyến tính dạng:
# 
# $$k_1 \mathbf{a}_1 + k_2 \mathbf{a}_2 + \dots + k_n \mathbf{a}_n = \mathbf{b} \tag{1}$$
# 
# Nếu xét ma trận $\mathbf{A} = [\mathbf{a}_1, \mathbf{a}_2 \dots ,\mathbf{a}_n] \in \mathbb{R}^{m \times n}$ có các cột là những véc tơ $\mathbf{a}_i \in \mathbb{R}^{m}$. Khi đó tổ hợp tuyến tính có thể biểu diễn dưới dạng một phép nhân ma trận với véc tơ:
# 
# $$\mathbf{A}\mathbf{k} = \mathbf{b}$$
# 
# Lưu ý rằng biểu diễn tổ hợp tuyến tính đối với véc tơ $\mathbf{b}$ có thể là không duy nhất. Tập hợp tất cả các véc tơ $\mathbf{b}$ trong phương trình $(1)$ ở trên được gọi là _không gian sinh_ (_span space_) của hệ véc tơ $\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}$, kí hiệu $\text{span}(\mathbf{a}_1, \dots, \mathbf{a}_n)$
# 
# 
# 
# **Hệ véc tơ độc lập tuyến tính là gì?**
# 
# Một hệ véc tơ $\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}$ gồm các véc tơ khác 0 là độc lập tuyến tính nếu phương trình:
# 
# $$k_1 \mathbf{a}_1 + k_2 \mathbf{a}_2 + \dots + k_n \mathbf{a}_n = 0  \tag{2}$$
# 
# có một nghiệm duy nhất là $k_1 = k_2 = \dots = k_n = 0$
# 
# Trái lại, nếu tồn tại một nghiệm mà phần tử $k_j \neq 0$ thì hệ véc tơ là _phụ thuộc tuyến tính_.
# 
# **Một số tính chất của tổ hợp tuyến tính**
# 
# 1-. Một hệ véc tơ là phụ thuộc tuyến tính khi và chỉ khi tồn tại một véc tơ trong hệ là tổ hợp tuyến tính của những véc tơ còn lại. Thật vậy, giả sử hệ véc tơ là phụ thuộc tuyến tính, khi đó tồn tại một phần tử $k_j \neq 0$ sao cho phương trình $(2)$ được thoả mãn. Khi đó:
# 
# $$\mathbf{a}_j = \frac{-k_1}{k_j} \mathbf{a}_1 + \dots + \frac{-k_{j-1}}{k_{j}} \mathbf{a}_{j-1}+ \frac{-k_{j+1}}{k_j} \mathbf{a}_{j+1}+ \dots +\frac{-k_n}{k_j} \mathbf{a}_n \tag{3}$$
# 
# Như vậy $\mathbf{a}_{j}$ là tổ hợp tuyến tính của những véc tơ còn lại. Trong trường hợp phương trình $(3)$ được thoả mãn thì ta cũng suy ra được phương trình $(2)$ có nghiệm $k_j \neq 0$ và hệ véc tơ là _phụ thuộc tuyến tính_.
# 
# 2-. Tập con khác rỗng của một hệ véc tơ độc lập tuyến tính là một hệ độc lập tuyến tính.
# 
# 3-. Tập hợp các dòng hoặc cột của một ma trận khả nghịch sẽ tạo thành một hệ các véc tơ độc lập tuyến tính.
# 
# 4-. Nếu $\mathbf{A}$ là một ma trận cao chiều, tức số hàng lớn hơn số cột thì tồn tại véc tơ $\mathbf{b}$ sao cho $\mathbf{A}\mathbf{x} = \mathbf{b}$ vô nghiệm.
# 
# 5-. Nếu $n > m$ thì $n$ véc tơ bất kì trong không gian $m$ chiều tạo thành một hệ véc tơ phụ thuộc tuyến tính.
# 
# ## 1.10. Cơ sở của một không gian
# 
# Một hệ các véc tơ $\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n \}$ trong không gian véc tơ $m$ chiều, kí hiệu là $V = \mathbb{R}^{m}$ được gọi là một cơ sở (_basic_) nếu như điều kiện kiện sau được thoả mãn:
# 
# 1. $V \equiv \text{span}(\mathbf{a}_1, \dots, \mathbf{a}_n)$
# 
# 2. ${\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n}$ là một hệ véc tơ độc lập tuyến tính.
# 
# Mỗi một véc tơ đều có một biểu diễn duy nhất dưới dạng một tổ hợp tuyển tính của những véc tơ của các $\mathbf{a}_i$.
# 
# ## 1.11. Biến đổi hệ cơ sở của véc tơ
# 
# Trong không gian $m$ chiều thì mọi véc tơ đều có thể biểu diễn thông qua hệ véc tơ đơn vị $(\mathbf{e}_1, \mathbf{e}_2, \dots , \mathbf{e}_m)$. Trong đó véc tơ $\mathbf{e}_i$ được gọi là véc tơ đơn vị có phần tử thứ $i$ là 1, các phần tử còn lại bằng 0.
# 
# Bản chất của một phép nhân ma trận với một véc tơ là một phép biến đổi hệ cơ sở mà ở đó mỗi một cột của ma trận được xem như một véc tơ cơ sở. Giả sử ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ nhân với véc tơ $\mathbf{x}\in \mathbb{R}^{n}$.
# 
# $$\mathbf{A} \mathbf{x} = \mathbf{a}^{(1)} x_1 + \mathbf{a}^{(2)} x_2 + \dots + \mathbf{a}^{(m)}  x_m = \mathbf{y}$$
# 
# Trong đó $\mathbf{a}^{(i)}$ có thể được xem như là một véc tơ cột thứ $i$ của ma trận $\mathbf{A}$. Ta có thể xem như véc tơ $\mathbf{y}$ được biểu diễn thông qua các véc tơ cơ sở cột mà toạ độ tương ứng với mỗi chiều trong hệ cơ sở là các $x_i$.
# 
# ## 1.12. Range và Null space
# 
# Với mỗi ma trận $\mathbf{A} \in \mathbb{R}^{m×n}$, có hai không gian con quan trọng ứng với ma trận này.
# 
# 1. Range của ma trận $\mathbf{A}$ được định nghĩa là tập hợp tất cả các điểm là tổ hợp tuyến tính của các cột của ma trận $\mathbf{A}$:
# 
# $$\mathcal{R}(\mathbf{A}) = \{\mathbf{y} \in \mathbb{R}^m : \exists x \in \mathbb{R}^n , \mathbf{A}\mathbf{x} = \mathbf{y} \}$$
# 
# $\mathcal{R}(\mathbf{A})$ còn chính là không gian sinh (_span_) của các cột của ma trận $\mathbf{A}$. $\mathcal{R}(\mathbf{A})$ là một không gian con của $\mathbb{R}^m$ với số chiều chính bằng số lượng lớn nhất các cột của $\mathbf{A}$ độc lập tuyến tính.
# 
# 2. Null của $\mathbf{A}$, ký hiệu là $\mathcal{N}(\mathbf{A})$, được định nghĩa là:
# 
# $$\mathcal{N}(\mathbf{A}) = \{ \mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = 0 \}$$
# 
# Mỗi véc tơ trong $\mathcal{N}(\mathbf{A})$ chính là một bộ các hệ số làm cho tổ hợp tuyến tính các cột của $\mathbf{A}$ tạo thành một véc tơ $0$. $\mathcal{N} (\mathbf{A})$ có thể được chứng minh là một không gian con trong $\mathbb{R}^n$ . Khi các cột của $\mathbf{A}$ là độc lập tuyến tính, theo định nghĩa, $\mathcal{N}(\mathbf{A}) = \{ 0 \}$ (chỉ gồm véc tơ $0$).
# 
# $\mathcal{R}(\mathbf{A})$ và $\mathcal{N} (\mathbf{A})$ là các không gian con véc tơ với số chiều lần lượt là $\dim(\mathcal{R}(\mathbf{A}))$ và
# $\dim(\mathcal{N} (\mathbf{A}))$, ta có tính chất quan trọng sau đây:
# 
# $$\dim(\mathcal{R}(\mathbf{A})) + \dim(\mathcal{N} (\mathbf{A})) = n$$
# 
# ## 1.13. Hạng của ma trận
# 
# Xét một ma trận $\mathbf{A} ∈ \mathbb{R}^{m×n}$ . _Hạng_ (_rank_) của ma trận của ma trận được ký hiệu là $\text{rank}(\mathbf{A})$, được định nghĩa là số lượng lớn nhất các cột hoặc dòng của nó tạo thành một hệ độc lập tuyến tính.
# 
# **Các tính chất quan trọng của hạng:**
# 
# 1. Một ma trận có hạng bằng 0 khi và chỉ khi nó là ma trận 0.
# 2. $\text{rank}(\mathbf{A}) = \text{rank}(\mathbf{A}^{\intercal})$. Hạng của một ma trận bằng hạng của ma trận chuyển vị. Nói cách khác, số lượng lớn nhất các cột độc lập tuyến tính của một ma trận bằng với số lượng
# lớn nhất các hàng độc lập tuyến tính của ma trận đó. Từ đây ta suy ra:
# 3. Nếu $\mathbf{A} \in \mathbb{R}^{m×n}$ , thì $\text{rank}(\mathbf{A}) \leq \min(m, n)$ vì theo định nghĩa, hạng của một ma trận không thể lớn hơn số hàng hoặc số cột của nó.
# 4. $\text{rank}(\mathbf{AB}) \leq \min(\text{rank}(\mathbf{A}), \text{rank}(\mathbf{B}))$
# 5. $\text{rank}(\mathbf{A} + \mathbf{B}) ≤ \text{rank}(\mathbf{A}) + \text{rank}(\mathbf{B})$. Điều này chỉ ra rằng một ma trận có hạng bằng $k$ không được biểu diễn dưới dạng ít hơn k ma trận có hạng bằng 1. Đến bài Singular Value
# Decomposition, chúng ta sẽ thấy rằng một ma trận có hạng bằng $k$ có thể biểu diễn được dưới dạng đúng k ma trận có hạng bằng 1.
# 6. Bất đẳng thức Sylvester về hạng: Nếu $\mathbf{A} \in \mathbb{R}^{m×n} , \mathbf{B} \in \mathbb{R}^{n×k}$ , thì $\text{rank}(\mathbf{A}) + \text{rank}(\mathbf{B}) − n ≤ \text{rank}(\mathbf{AB})$
# 
# # 2. Tóm tắt
# 
# Như vậy qua chương này mình đã hướng dẫn cho các bạn các kiến thức bản nhất trong đại số tuyến tính. Bao gồm:
# 
# 1. Các khái niệm: Số vô hướng, véc tơ, ma trận, tensor kèm theo thuộc tính của chúng.
# 2. Các phép tính cộng, trừ, nhân ma trận, nhân véc tơ, nhân ma trận với véc tơ.
# 3. Khái niệm về chuẩn và ý nghĩa của chúng trong vai trò một độ đo đối với véc tơ.
# 
# Đây là những kiến thức nền tảng nhưng rất quan trọng mà bạn đọc cần nắm vững trước khi học sâu về AI.
# 
# # 3. Bài tập
# 
# Một vài bài tập dưới đây sẽ giúp bạn ôn lại kiến thức tốt hơn:
# 
# 1. Khởi tạo một số vô hướng, một véc tơ có độ dài là $3$ và một ma trận bất kỳ có kích thước là $2\times 3$ trên pytorch.
# 2. Tính tích giữa ma trận và véc tơ ở câu 1.
# 3. Tính tổng các dòng và tổng các cột của ma trận ở câu 1.
# 4. Chứng minh rằng nếu $\mathbf{A}$ là một ma trận vuông thì $\mathbf{A} + \mathbf{A}^{\top}$ là một ma trận đối xứng.
# 5. Cho $\mathbf{A}, \mathbf{B}, \mathbf{C}$ là ba ma trận có kích thước lần lượt là $m \times n$, $n \times p$ và $p \times q$ chứng minh rằng $\mathbf{ABC} = (\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$
# 6. $\mathbf{trace}$ của ma trận là tổng các phần tử nằm trên đường chéo chính ( phần tử mà có index dòng bằng cột). Chứng minh rằng: $\mathbf{trace(AB) = trace(BA)}$
# 7. Chứng minh: $\mathbf{A} \odot \mathbf{(B+C)} = \mathbf{A} \odot \mathbf{B} + \mathbf{A} \odot \mathbf{C}$
# 8. Chứng minh: $\mathbf{A} \odot (\mathbf{B} \odot \mathbf{C})= (\mathbf{A} \odot \mathbf{B}) \odot \mathbf{C}$
# 9. Chứng mình rằng: $(\mathbf{A}\mathbf{B})^{\intercal} = \mathbf{B}^{\intercal}\mathbf{A}^{\intercal}$
# 10. Chứng minh: $\mathbf{A}\mathbf{I} = \mathbf{A}$. Trong đó $\mathbf{I}$ là ma trận đơn vị.
