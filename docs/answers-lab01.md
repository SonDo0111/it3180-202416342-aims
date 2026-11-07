# Lab 01 – Câu hỏi thảo luận

**Câu hỏi nhanh:** Cấu hình '--global' được lưu ở đâu? Khác gì với '--local'?

- Cấu hình `--global` lưu trong tệp `~/.gitconfig` của người dùng hiện tại. Cấu hình này áp dụng cho toàn bộ các repo của người dùng hiện tại.
- Cấu hình `--local` (mặc định khi đứng trong một repo) lưu trong `.git/config` của **chỉ repo đó**, và ghi đè giá trị `--global` (thứ tự ưu tiên: `--system` < `--global` < `--local`).

**Câu 1:** Vì sao dùng git mv?

`git mv` thực hiện thao tác đổi vị trí/đổi tên tệp và cập nhật trạng thái trong working tree/staging.
Git vẫn lưu lịch sử theo commit; khi xem bằng `git log --follow -- <file>`, Git có thể nhận diện nội dung tệp được chuyển sang đường dẫn mới.
Về bản chất, Git phát hiện rename dựa trên độ tương đồng nội dung khi so sánh commit, nên `git mv` không tạo ra một loại đối tượng lịch sử đặc biệt; nó giúp thao tác rõ ràng và giảm nguy cơ quên `git add` đường dẫn mới/xóa đường dẫn cũ.

**Câu 2:** release/lab01 có phải baseline?

Có.
Theo quy trình bài thực hành, nhánh `release/lab01` được tạo từ `master` sau khi Lab 01 hoàn tất và đại diện cho trạng thái bài nộp đã thống nhất.
Nó là một baseline có thể tham chiếu/tái tạo.
Trong Lab 01 chưa thực hiện gắn tag phiên bản chính thức; tag được thực hành ở Lab 04.

**Câu 3:** Vì sao không commit thẳng master dù làm một
mình?

Vì mục tiêu là tuân thủ quy trình kiểm soát thay đổi: thay đổi đi qua nhánh có mục đích, Pull Request, kiểm tra diff và CI/review trước khi tích hợp. Làm một mình vẫn có thể tự kiểm tra PR; branch protection giúp ngăn thao tác trực tiếp và tạo lịch sử có thể kiểm toán. Điều này giữ quy trình nhất quán khi làm nhóm.
