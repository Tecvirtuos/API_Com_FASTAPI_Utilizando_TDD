from store.usecases.product import product_usecases


async def test_usecases_should_return_sucess(product_in):
    result = await product_usecases.create(body=product_in)

    # assert isinstance(result, ProductOut)
    assert result is None
