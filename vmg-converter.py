from src.vmg import VMG
from src.vmg2xml import vmg2xml
import click


@click.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--params', '-p', multiple=True, help='Custom vbody params')
def converter(filepath, params):
    CUSTOM_VBODY_PARAMS = [*params]
    vmg = VMG(CUSTOM_VBODY_PARAMS)
    vmg_list = vmg.load(filepath)
    vmg2xml(vmg_list, filepath + ".xml")
    print("Success! {}.xml has been created.".format(filepath))


if __name__ == "__main__":
    converter()
