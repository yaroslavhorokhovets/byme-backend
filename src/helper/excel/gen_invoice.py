#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter


def gen_invoice(path, data):
    """
    :param path: path save file
    :param data: format:
        {
            "facility_name": "",
            "number_released": "",
            "sales_staff": "",
            "date_upload_invoice": "",
            "total": "",
            "filters": [],
            "subtotal": "",
            "tax": "",
        }
    :return:
    """
    font_1 = "Yu Gothic"
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:Q', 4.83)
    # header
    worksheet.merge_range(
        "A1:Q1",
        "領　収　書",
        workbook.add_format(
            {
                'align': 'center',
                'valign': 'vcenter',
                'font': font_1,
                'size': 18
            }
        )
    )

    format1 = workbook.add_format()
    format1.set_align('center')
    format1.set_valign('vcenter')
    format1.set_size(16)
    format1.set_bottom(1)
    worksheet.merge_range(
        "A3:G3",
        data.get("facility_name", "Bymeグランドホテル"),
        format1
    )
    format2 = workbook.add_format()
    format2.set_size(14)
    format2.set_font(font_1)
    worksheet.merge_range(
        "H3:I3",
        "御中",
        format2
    )

    format3 = workbook.add_format()
    format3.set_font(font_1)
    format3.set_size(12)
    worksheet.merge_range(
        "L3:M3",
        "領収書No.",
        format3
    )
    format4 = workbook.add_format()
    format4.set_align("right")
    format4.set_font(font_1)
    format4.set_size(12)
    worksheet.merge_range(
        "N3:Q3",
        data.get("number_released", 0),
        format4
    )
    format5 = workbook.add_format()
    format5.set_font(font_1)
    format5.set_size(12)
    worksheet.merge_range(
        "A4:G4",
        data.get("sales_staff", ""),
        format5
    )
    format6 = workbook.add_format()
    format6.set_font(font_1)
    format6.set_size(12)
    worksheet.merge_range(
        "L4:M4",
        "発行日",
        format6
    )

    format7 = workbook.add_format()
    format7.set_align("right")
    format7.set_size(12)
    worksheet.merge_range(
        "N4:Q4",
        data.get("date_upload_invoice", "yyyy/mm/dd"),
        format7
    )

    format8 = workbook.add_format()
    format8.set_align("center")
    format8.set_align('vcenter')
    format8.set_bottom(6)
    format8.set_bold()
    format8.set_font(font_1)
    format8.set_size(14)
    worksheet.merge_range(
        "A6:B6",
        "件名:",
        format8
    )
    format9 = workbook.add_format()
    format9.set_align('left')
    format9.set_bottom(6)
    format9.set_bold()
    format9.set_size(14)
    worksheet.merge_range(
        "C6:I6",
        "Byme利用料 {}".format(data.get("invoice_month")),
        format9
    )
    format10 = workbook.add_format()
    format10.set_align('left')
    format10.set_size(12)
    worksheet.merge_range(
        "K6:Q6",
        "Byme",
        format10
    )
    format11 = workbook.add_format()
    format11.set_align('left')
    format11.set_size(12)
    worksheet.merge_range(
        "K7:Q7",
        "〒246-0031",
        format10
    )

    format12 = workbook.add_format()
    format12.set_align('right')
    format12.set_valign('vcenter')
    format12.set_bottom(6)
    format12.set_bold()
    format12.set_size(14)
    format12.set_font(font_1)
    worksheet.merge_range(
        "A8:B9",
        "合計金額",
        format12
    )
    format13 = workbook.add_format()
    format13.set_align('center')
    format13.set_valign('vcenter')
    format13.set_bottom(6)
    format13.set_bold()
    format13.set_size(14)
    format13.set_font(font_1)
    worksheet.merge_range(
        "C8:G9",
        "¥" + str(data["total"]),
        format13
    )

    format14 = workbook.add_format()
    format14.set_align('center')
    format14.set_valign('vcenter')
    format14.set_bottom(6)
    format14.set_bold()
    format13.set_size(12)
    format13.set_font(font_1)
    worksheet.merge_range(
        "H8:I9",
        "（税込）",
        format14
    )
    format15 = workbook.add_format()
    format15.set_align('left')
    format15.set_size(12)
    worksheet.merge_range(
        "K8:Q8",
        "神奈川県横浜市瀬谷区瀬谷4-18-6",
        format15
    )

    format16 = workbook.add_format()
    format16.set_align('left')
    format16.set_size(12)
    worksheet.merge_range(
        "K9:Q9",
        "グリーングラスB102号室",
        format16
    )

    format17 = workbook.add_format()
    format17.set_align('right')
    format17.set_size(12)
    worksheet.merge_range(
        "K10:L10",
        "TEL:",
        format17
    )
    format18 = workbook.add_format()
    format18.set_align('right')
    format18.set_size(12)
    worksheet.merge_range(
        "K11:L11",
        "E-Mail:",
        format18
    )
    format19 = workbook.add_format()
    format19.set_align('right')
    format19.set_size(12)
    worksheet.merge_range(
        "K12:L12",
        "担当:",
        format19
    )
    format20 = workbook.add_format()
    format20.set_align('left')
    format20.set_size(12)
    worksheet.merge_range(
        "M10:Q10",
        "090-2248-7747",
        format20
    )
    format21 = workbook.add_format()
    format21.set_align('left')
    format21.set_underline(1)
    format21.set_color("blue")
    format21.set_size(12)
    worksheet.merge_range(
        "M11:Q11",
        "yuhi_oshima@app-byme.com",
        format21
    )
    format22 = workbook.add_format()
    format22.set_align('left')
    format22.set_size(12)
    worksheet.merge_range(
        "M12:Q12",
        "大島　勇飛",
        format22
    )

    format23 = workbook.add_format()
    format23.set_border(1)
    format23.set_valign("center")
    format23.set_bold()
    format23.set_bg_color("#BFEFFF")
    format23.set_size("12")
    format23.set_font("Yu Gothic")
    format23.set_valign('vcenter')
    worksheet.write(
        "A15",
        "No .",
        format23
    )
    worksheet.merge_range(
        "B15:I15",
        "摘要",
        format23
    )
    worksheet.merge_range(
        "J15:K15",
        "数量",
        format23
    )
    worksheet.merge_range(
        "L15:N15",
        "単価",
        format23
    )
    worksheet.merge_range(
        "O15:Q15",
        "金額",
        format23
    )
    start_row = 16
    for fil in data["filters"]:
        worksheet.write(
            "A{}".format(start_row),
            str(start_row - 15),
            workbook.add_format(
                {
                    'align': 'right',
                    'border': 1
                }
            )
        )
        worksheet.merge_range(
            "B{}:I{}".format(start_row, start_row),
            fil["name"],
            workbook.add_format(
                {
                    'align': 'left',
                    'border': 1
                }
            )
        )
        worksheet.write(
            "J{}".format(start_row),
            fil["number"],
            workbook.add_format(
                {
                    'align': 'center',
                    'border': 1
                }
            )
        )
        worksheet.write(
            "K{}".format(start_row),
            fil["unit"],
            workbook.add_format(
                {
                    'align': 'center',
                    'border': 1
                }
            )
        )
        worksheet.merge_range(
            "L{}:N{}".format(start_row, start_row),
            fil["price"],
            workbook.add_format(
                {
                    'align': 'right',
                    'border': 1
                }
            )
        )
        worksheet.merge_range(
            "O{}:Q{}".format(start_row, start_row),
            "¥" + str(fil["money"]),
            workbook.add_format(
                {
                    'align': 'right',
                    'border': 1
                }
            )
        )
        start_row += 1

    worksheet.merge_range(
        "J{}:K{}".format(start_row, start_row),
        "小計",
        format23
    )
    worksheet.merge_range(
        "L{}:Q{}".format(start_row, start_row),
        "¥" + str(data["subtotal"]),
        workbook.add_format({
            "align": "right",
            'border': 1
        })
    )
    worksheet.merge_range(
        "J{}:K{}".format(start_row + 1, start_row + 1),
        "消費税",
        format23
    )
    worksheet.merge_range(
        "L{}:Q{}".format(start_row + 1, start_row + 1),
        "¥" + str(data["tax"]),
        workbook.add_format({
            "align": "right",
            'border': 1
        })
    )
    worksheet.merge_range(
        "J{}:K{}".format(start_row + 2, start_row + 2),
        "合計",
        format23
    )
    worksheet.merge_range(
        "L{}:Q{}".format(start_row + 2, start_row + 2),
        "¥" + str(data["total"]),
        workbook.add_format({
            "align": "right",
            'bold': 1,
            'border': 1
        })
    )

    worksheet.merge_range(
        "A{}:B{}".format(start_row + 4, start_row + 8),
        "備考",
        format23
    )
    worksheet.merge_range(
        "C{}:Q{}".format(start_row + 4, start_row + 8),
        "",
        workbook.add_format({
            'border': 1
        })
    )

    workbook.close()


if __name__ == '__main__':
    data = {
        "total": 53130,
        "tax": 4830,
        "subtotal": 48300,
        "filters": [
            {
                "name": "アカウント発行料",
                "number": 1,
                "unit": "式",
                "price": "3000",
                "money": "3000"
            },
            {
                "name": "年間利用料",
                "number": 1,
                "unit": "年",
                "price": "19800",
                "money": "19800"
            },
            {
                "name": "編集依頼料",
                "number": 35,
                "unit": "枚",
                "price": "100",
                "money": "3500"
            },
            {
                "name": "即納依頼料",
                "number": 5,
                "unit": "枚",
                "price": "400",
                "money": "2000"
            },
            {
                "name": "オプション機材料",
                "number": 1,
                "unit": "式",
                "price": "20000",
                "money": "20000"
            }
        ]
    }
    gen_invoice("test1.xlsx", data)
