# CHANGELOG

## [Unreleased]

## [1.1.0] - 2026-11-07

### Added

- `search_by_category()` trong `aims/search.py`.
- `Cart.sort_by_title()` và `Cart.sort_by_cost()`.

## [1.0.0] - 2026-11-07

### Added

- Thêm hàm `print_cart` vào class `Cart` để hiển thị chi tiết giỏ hàng và xử lý trường hợp giỏ hàng trống.
- Thêm chức năng hiển thị chi tiết giỏ hàng vào chương trình demo (`main.py`).
- Thêm tính năng tìm kiếm đĩa theo tiêu đề (`search_by_title`).
- Thêm sơ đồ Use Case (`use-case.md`) vào tài liệu.
- Thêm hàm tính toán tổng tiền sau khi giảm giá (`total_cost_with_discount`).
- Thêm thông báo bằng tiếng Việt khi đưa đĩa vào giỏ hàng.
- Thêm template cho Pull Request (`.github/pull_request_template.md`).

### Fixed

- Sửa lỗi giỏ hàng tiếp nhận đĩa thứ 21 (vượt quá `MAX_NUMBER_ORDERED`).
- Thêm test case để tái hiện lỗi vượt quá giới hạn đĩa trong giỏ hàng.
- Sửa lỗi tính toán giảm giá, trả về tổng tiền sau khi giảm và validate giá trị phần trăm.

### Removed / Reverted

- Hủy bỏ (revert) tính năng hiển thị cụ thể tên đĩa khi thêm vào giỏ hàng (`feat: show added title`) do phát sinh vấn đề sau khi merge.
