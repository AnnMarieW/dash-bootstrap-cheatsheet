"""
This is the index that links the name of the item in the cheatsheet cards
with the code and preview content for the offcanvas component.
See the content folder for details.
"""


from content.utility_border import *
from content.utility_color import *
from content.utility_display import *
from content.utility_spacing import *
from content.utility_opacity import *
from content.utility_position import *
from content.utility_text import *
from content.utility_misc import *
from content.utility_flex import *
from content.utility_grid import *


examples = {
    # Utility border examples
    "border": [border_code, border_preview],
    "border-{direction}": [border_direction_code, border_direction_preview],
    "border-0": [border_0_code, border_0_preview],
    "border-{direction}-0": [border_direction_0_code, border_direction_0_preview],
    "border-{color}": [border_color_code, border_color_preview],
    "border-{size}": [border_size_code, border_size_preview],
    "rounded": [border_rounded_code, border_rounded_preview],
    "rounded-{corner}": [border_rounded_corner_code, border_rounded_corner_preview],
    "rounded-{size}": [border_rounded_size_code, border_rounded_size_preview],
    #
    # Utility color examples
    "text-{color}": [text_color_code, text_color_preview],
    "text-body": [text_body_code, text_body_preview],
    "text-muted": [text_muted_code, text_muted_preview],
    "text-black-50": [text_black_50_code, text_black_50_preview],
    "text-white-50": [text_white_50_code, text_white_50_preview],
    "bg-{color}": [bg_color_code, bg_color_preview],
    "bg-transparent": [bg_transparent_code, bg_transparent_preview],
    "bg-gradient": [bg_gradient_code, bg_gradient_preview],
    #
    # Utility display examples
    "d-*-none": [d_none_code, d_none_preview],
    "d-*-inline": [d_inline_code, d_inline_preview],
    "d-*-inline-block": [d_inline_block_code, d_inline_block_preview],
    "d-*-block": [d_block_code, d_block_preview],
    "d-*-grid": [d_grid_code, d_grid_preview],
    "d-*-flex": [d_flex_code, d_flex_preview],
    "d-*-inline-flex": [d_inline_flex_code, d_inline_flex_preview],
    "d-print-{display}": [d_print_display_code, d_print_display_preview],
    #
    # Utility Spacing examples
    "m-*-{option}": [m_code, m_preview],
    "mt-*-{option}": [mt_code, mt_preview],
    "me-*-{option}": [me_code, me_preview],
    "mb-*-{option}": [mb_code, mb_preview],
    "ms-*-{option}": [ms_code, ms_preview],
    "mx-*-{option}": [mx_code, mx_preview],
    "my-*-{option}": [my_code, my_preview],
    "p-*-{option}": [p_code, p_preview],
    "pt-*-{option}": [pt_code, pt_preview],
    "pe-*-{option}": [pe_code, pe_preview],
    "pb-*-{option}": [pb_code, pb_preview],
    "ps-*-{option}": [ps_code, ps_preview],
    "px-*-{option}": [px_code, px_preview],
    "py-*-{option}": [py_code, py_preview],
    "gap-*-{size}": [gap_code, gap_preview],
    #
    # Utility opacity examples
    "text-opacity-{value}": [text_opacity_code, text_opacity_preview],
    "bg-opacity-{value}": [bg_opacity_code, bg_opacity_preview],
    "opacity-{value}": [opacity_code, opacity_preview],
    #
    # Utility position examples
    "float-*-{option}": [float_code, float_preview],
    "position-{option}": [position_code, position_preview],
    "{direction}-{position}": [direction_position_code, direction_position_preview],
    "translate-middle": [translate_middle_code, translate_middle_preview],
    "translate-middle-{direction}": [
        translate_middle_direction_code,
        translate_middle_direction_preview,
    ],
    "align-{option}": [align_code, align_preview],
    "vstack": [vstack_code, vstack_preview],
    "hstack": [hstack_code, hstack_preview],
    "vr (vertical rule)": [vr_code, vr_preview],
    #
    # Utility text examples
    "text-*-start": [text_start_code, text_start_preview],
    "text-*-center": [text_center_code, text_center_preview],
    "text-*-end": [text_end_code, text_end_preview],
    "text-wrap": [text_wrap_code, text_wrap_preview],
    "text-nowrap": [text_nowrap_code, text_nowrap_preview],
    "text-break": [text_break_code, text_break_preview],
    "text-{option}": [text_option_code, text_option_preview],
    "fs-{size}": [fs_size_code, fs_size_preview],
    "fw-{weight}": [fw_weight_code, fw_weight_preview],
    "fst-{style}": [fst_style_code, fst_style_preview],
    "lh-{style}": [lh_style_code, lh_style_preview],
    "font-monospace": [font_monospace_code, font_monospace_preview],
    "text-reset": [text_reset_code, text_reset_preview],
    "text-decoration-{option}": [text_decoration_code, text_decoration_preview],
    #
    # Utility misc examples
    "user-select-{option}": [user_select_code, user_select_preview],
    "pe-{option} (pointer)": [pointer_code, pointer_preview],
    "overflow-option": [overflow_code, overflow_preview],
    "shadow/shadow-{option}": [shadow_code, shadow_preview],
    "w-{option}": [w_option_code, w_option_preview],
    "h-{option}": [h_option_code, h_option_preview],
    "mw-100": [mw_100_code, mw_100_preview],
    "mh-100": [mh_100_code, mh_100_preview],
    "viewport": [viewport_code, viewport_preview],
    "visible/invisible": [visible_code, visible_preview],
    #
    # Utility flex examples
    "flex-*-row": [flex_row_code, flex_row_preview],
    "flex-*-row-reverse": [flex_row_reverse_code, flex_row_reverse_preview],
    "flex-*-column": [flex_column_code, flex_column_preview],
    "flex-*-column-reverse": [flex_column_reverse_code, flex_column_reverse_preview],
    "justify-content-*-{option}": [justify_content_code, justify_content_preview],
    "align-items-*-{option}": [align_items_code, align_items_preview],
    "align-self-*-{option}": [align_self_code, align_self_preview],
    "flex-*-fill": [flex_fill_code, flex_fill_preview],
    "flex-grow-{option}": [flex_grow_code, flex_grow_preview],
    "flex-shrink-{option}": [flex_shrink_code, flex_shrink_preview],
    "flex-*-nowrap": [flex_nowrap_code, flex_nowrap_preview],
    "flex-*-wrap": [flex_wrap_code, flex_wrap_preview],
    "flex-*-wrap-reverse": [flex_wrap_reverse_code, flex_wrap_reverse_preview],
    "order-*-{order-number}": [order_number_code, order_number_preview],
    "order-*-{order-name}": [order_name_code, order_name_preview],
    "align-content-*-{option}": [align_content_code, align_content_preview],
    #
    # Utilites Grid examples
    "gx-{size}": [gx_size_code, gx_size_preview],
    "gx-*-{size}": [gx_dev_size_code, gx_dev_size_preview],
    "gy-{size}": [gy_size_code, gy_size_preview],
    "gy-*-{size}": [gy_dev_size_code, gy_dev_size_preview],
    "g-{size}": [g_size_code, g_size_preview],
    "g-*-{size}": [g_dev_size_code, g_dev_size_preview],
}
