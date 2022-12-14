import pytest
from numi import spell_out


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            (1, None),
            [
                [1, "et_hk_ef", ["eins"]],
                [1, "et_hk_nf", ["eitt"]],
                [1, "et_hk_þf", ["eitt"]],
                [1, "et_hk_þgf", ["einu"]],
                [1, "et_kk_ef", ["eins"]],
                [1, "et_kk_nf", ["einn"]],
                [1, "et_kk_þf", ["einn"]],
                [1, "et_kk_þgf", ["einum"]],
                [1, "et_kvk_ef", ["einnar"]],
                [1, "et_kvk_nf", ["ein"]],
                [1, "et_kvk_þf", ["eina"]],
                [1, "et_kvk_þgf", ["einni"]],
                [1, "ft_hk_ef", ["einna"]],
                [1, "ft_hk_nf", ["ein"]],
                [1, "ft_hk_þf", ["ein"]],
                [1, "ft_hk_þgf", ["einum"]],
                [1, "ft_kk_ef", ["einna"]],
                [1, "ft_kk_nf", ["einir"]],
                [1, "ft_kk_þf", ["eina"]],
                [1, "ft_kk_þgf", ["einum"]],
                [1, "ft_kvk_ef", ["einna"]],
                [1, "ft_kvk_nf", ["einar"]],
                [1, "ft_kvk_þf", ["einar"]],
                [1, "ft_kvk_þgf", ["einum"]],
            ],
        ),
    ],
)
def test_decimals(test_input, expected):
    assert spell_out(test_input[0], test_input[1]) == expected
