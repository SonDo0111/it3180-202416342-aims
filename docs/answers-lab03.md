# Lab 03 – Câu hỏi thảo luận

**Câu 1:** Merge base là gì?

- Là commit tổ tiên chung gần nhất của hai nhánh, tức điểm mà hai nhánh bắt đầu tách ra (xem bằng `git merge-base A B`).
- Git dùng nó làm mốc để merge ba chiều (base, bên mình, bên kia): so từng bên với base để biết bên nào đã đổi gì.
- Chỉ một bên đổi một dòng thì lấy bên đó; cả hai bên cùng đổi một dòng so với base thì xung đột (như hai dòng print trong `add_dvd`).
- Với PR, merge base quyết định diff hiển thị. Chọn sai base (ví dụ bugfix từ feature nhưng base là master) thì PR lẫn cả commit của feature.

**Câu 2:** Vì sao `master`/`release/*` phải dùng `revert`?

- `master` và `release/*` là lịch sử chung, đã được người khác kéo về và dựa vào. `reset` viết lại lịch sử, buộc phải force-push và làm lịch sử của mọi người phân kỳ; branch protection cũng chặn việc này.
- `revert` không sửa commit cũ mà thêm một commit đảo ngược, nên lịch sử chỉ tiến lên, truy vết được cái gì đã hoàn tác và vì sao, và đi qua PR có review.
- Với merge commit phải dùng `-m 1` để chọn cha thứ nhất (master) làm mốc, giữ lại phần của master và gỡ phần của nhánh đã merge.
- `reset` chỉ dùng cho commit chưa push.
