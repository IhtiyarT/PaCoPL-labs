from behave import when, then
from main import get_result


@when('User passes arguments "{args}"')
def step_impl(context, args):
    coef_list = [int(i) for i in args.split()]
    context.response = get_result(coef_list[0], coef_list[1], coef_list[2])


@then('Result is "{result}')
def step_impl(context, result):
    assert ({float(i) for i in result.split()} == context.response)

