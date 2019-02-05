"""
Convert from parse tree to universal dependencies

Usage:
    negbio_pipeline ptb2ud [options] --output=<directory> <file> ...

Options:
    --output=<directory>    Specify the output directory.
    --suffix=<suffix>       Append an additional SUFFIX to file names. [default: .ud.xml]
    --verbose               Print more information about progress.
"""
from negbio.cli_utils import parse_args
from negbio.pipeline.ptb2ud import NegBioPtb2DepConverter
from negbio.pipeline.scan import scan_document

if __name__ == '__main__':
    argv = parse_args(__doc__)
    ptb2dep = NegBioPtb2DepConverter(universal=True)
    scan_document(source=argv['<file>'], directory=argv['--output'], suffix=argv['--suffix'],
                  fn=NegBioPtb2DepConverter.convert_doc, non_sequences=[])