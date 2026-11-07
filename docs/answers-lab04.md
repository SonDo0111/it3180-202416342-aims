# Lab 04 - Câu hỏi thảo luận

**Câu 1:** Vì sao chuẩn bị phát hành trên `master` trước, không sửa trên nhánh release?

Mọi nội dung dự kiến thuộc phiên bản phát hành (version trong package, CHANGELOG, tài liệu) cần được review và merge vào dòng phát triển chính trước.
Sau đó tạo `release/lab04` từ trạng thái master đã hoàn chỉnh để nhánh release đóng băng đúng baseline.
Nếu chỉnh sửa trực tiếp trên release, master sẽ không có cùng trạng thái phát hành và quy trình lại cần đồng bộ ngược, mâu thuẫn yêu cầu của tài liệu.

**Câu 2:** Vì sao `release/*` không merge vào `master`?

- `release/*` là baseline đã đóng băng, chỉ chứa đúng thứ đã phát hành. `master` đã đi tiếp (ví dụ có `sort_by_cost`, đang ở `[Unreleased]`), nên merge ngược sẽ kéo các commit riêng của nhánh release (như commit nâng phiên bản 1.0.1 sau này) vào master và gây xung đột phiên bản.
- Mọi thay đổi vốn đã đi từ master ra release, nên master luôn là nguồn gốc; chỉ cần đưa bản vá sang bằng `cherry-pick -x` khi cần.
- Giữ lịch sử một chiều giúp truy vết rõ "bản phát hành chứa gì" bằng `git log A..B`.

**Câu 3:** So sánh với GitFlow

|                                   | Release Flow (học phần)                                          | GitFlow                                                                      |
| --------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Nhánh dài hạn                     | Chỉ `master` (+ các `release/*` để bảo trì)                      | `main` (bản đã phát hành) + `develop` (tích hợp)                             |
| Tính năng merge vào               | `master`                                                         | `develop`                                                                    |
| Nhánh release                     | Cắt từ `master`, **không merge lại**, sống tiếp làm dòng bảo trì | Cắt từ `develop`, ổn định xong thì **merge vào `main` và `develop`** rồi xóa |
| Hotfix                            | Từ `release/*`, đưa về `release/*` + `master` (cherry-pick)      | Từ `main`, merge vào `main` + `develop`                                      |
| Tag                               | Trên nhánh release                                               | Trên `main`                                                                  |
| Bảo trì nhiều phiên bản song song | Tự nhiên (mỗi phiên bản một nhánh `release/*`)                   | Khó: `main` chỉ có một dòng phiên bản mới nhất                               |
| Độ phức tạp                       | Ít nhánh, ít merge                                               | Nhiều nhánh, merge hai chiều                                                 |

GitFlow hợp với phát hành định kỳ, một phiên bản đang dùng

Release Flow hợp với việc cần giữ nhiều bản phát hành sống song song (mỗi tuần một `release/labXX`, có thể hotfix bản cũ).

**Câu 4:** Vì sao lên `1.0.0` mà không phải `0.4.0`?

- SemVer: `0.y.z` là giai đoạn đầu, API chưa ổn định. `1.0.0` đánh dấu bản đầu tiên coi là hoàn chỉnh, có hợp đồng tương thích.
- Sau Lab 01–03, AIMS-mini đã có đủ tính năng cốt lõi (giỏ hàng, tìm kiếm, giảm giá), có test và đã sửa lỗi lớn, nên đủ điều kiện công bố ổn định.
- Từ 1.0.0, sửa lỗi tăng PATCH (1.0.1), thêm tính năng tương thích tăng MINOR (1.1.0).
