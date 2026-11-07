# Lab 02 – Câu hỏi thảo luận

**Câu 1:** Vì sao phải đồng bộ `master` trước khi tạo/gửi PR?

Nhánh tính năng có thể được tạo từ một phiên bản `master` cũ.
Trong lúc phát triển, `master` có thể nhận thay đổi mới từ PR khác.
Đồng bộ bằng `fetch` rồi `merge origin/master` (hoặc rebase khi nhánh riêng và phù hợp) giúp phát hiện xung đột sớm, kiểm thử trên trạng thái tích hợp gần nhất và giảm nguy cơ PR gây lỗi khi merge.
Bài thực hành minh họa Dev 2 phải lấy thay đổi `print_cart` đã được merge trước khi gửi PR tìm kiếm.

**Câu 2:** Khi nào không được rebase?

Rebase tạo commit mới (SHA mới) thay cho commit cũ, tức là **viết lại lịch sử**.
Không rebase khi:

- Commit **đã được chia sẻ** và người khác có thể đã dựa vào: đã push lên nhánh dùng chung (`master`, `release/*`), hoặc nhánh mà đồng đội đang làm tiếp/đã tạo nhánh con từ đó (ví dụ `bugfix/*` tạo từ `feature/discount` ở Lab 03). Rebase khiến họ có lịch sử "song sinh", phải force-push và dễ mất commit.
- Nhánh đã mở PR và đang được review: SHA thay đổi làm mất ngữ cảnh comment, (với _dismiss stale approvals_) mất luôn approval.
- Lịch sử cần giữ đúng như đã xảy ra để kiểm toán (nhánh phát hành, tag).

Được rebase khi nhánh còn là **nhánh riêng, chưa ai dùng**; nếu đã push nhánh riêng thì dùng `git push --force-with-lease` (không dùng `--force`).

**Câu 3:**. `feature/*` khác `topic/*` ra sao?

Trong tài liệu, `feature/*` biểu diễn một tính năng sản phẩm có hành vi người dùng, ví dụ `feature/cart-print`, `feature/search-by-title`. `topic/*` là nhánh cho một chủ đề/công việc hỗ trợ hoặc thay đổi có phạm vi cụ thể, ví dụ `topic/pr-template`, `topic/use-case-diagram`. Cả hai đều được tạo từ `master`, có mục đích riêng và tích hợp qua PR; khác nhau chủ yếu ở ý nghĩa/tên gọi và phạm vi công việc.

## So sánh 3 kiểu merge

- **Merge commit**: giữ các commit chi tiết và tạo commit merge; lịch sử thể hiện nhánh phân kỳ/hội tụ, có thể revert cả merge bằng `git revert -m 1 <sha>`.
- **Squash and merge**: gom toàn bộ thay đổi PR thành một commit trên nhánh đích; lịch sử gọn, nhưng không giữ từng commit riêng lẻ của nhánh.
- **Rebase and merge**: đặt các commit của nhánh lên đầu nhánh đích, tạo SHA mới và lịch sử tuyến tính; cần tránh áp dụng với nhánh đã chia sẻ nếu việc viết lại lịch sử gây ảnh hưởng cộng tác viên.
