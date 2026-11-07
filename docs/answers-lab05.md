# Lab 05 – Câu hỏi thảo luận

**Câu 1:** Vì sao ở Phần A chưa gắn tag `v1.1.0`? Nếu đã gắn rồi thì phải làm gì?

Phần A mới chuẩn bị tính năng và tạo `release/lab05`, nhưng chưa hoàn tất hotfix và kiểm toán trên tất cả các dòng phiên bản. Chỉ gắn tag khi baseline phát hành thực sự sẵn sàng. Nếu đã công bố `v1.1.0`, tag là định danh bất biến của phiên bản đã phát hành, không nên di chuyển hoặc ghi đè; bản phát hành có sửa đổi tiếp theo phải tăng PATCH thành `v1.1.1`.

**Câu 2:** Ưu, nhược điểm của upstream first so với release first?

- **Upstream first**: tạo hotfix từ `master`, sửa và kiểm thử ở dòng phát triển chính trước, sau đó cherry-pick sang các release đang được bảo trì. Ưu điểm là master nhận sửa lỗi sớm, phù hợp sản phẩm phát triển liên tục. Nhược điểm là thay đổi trên master có thể phụ thuộc mã/tính năng mới chưa tồn tại ở release cũ, khiến cherry-pick khó hoặc cần điều chỉnh.
- **Release first**: tạo hotfix từ đúng nhánh release bị lỗi, sửa trong bối cảnh phiên bản đã phát hành, sau đó lan truyền commit sửa lỗi sang master và các release khác. Ưu điểm là sửa đúng baseline đang bị ảnh hưởng, phù hợp bài tập có nhiều bản phát hành song song. Nhược điểm là phải kiểm toán lan truyền cẩn thận để không bỏ sót nhánh; có thể cần xử lý khác biệt giữa các dòng phiên bản.

**Câu 3:** Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào phát hiện?
Để kiểm tra các commit trên `master` đã được lan truyền sang `release/lab05` hay chưa, dùng `git cherry -v origin/release/lab05 origin/master`. Dấu `+` chỉ commit trên master chưa có patch tương đương trong release/lab05 (cần xem xét lan truyền); dấu `-` chỉ commit có patch tương đương. Có thể kiểm tra bổ sung lịch sử cherry-pick bằng `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`.
