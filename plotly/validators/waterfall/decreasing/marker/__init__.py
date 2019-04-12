

import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self,
        plotly_name='line',
        parent_name='waterfall.decreasing.marker',
        **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Line'),
            data_docs=kwargs.pop(
                'data_docs', """
            color
                Sets the line color of all decreasing values.
            width
                Sets the line width of all decreasing values.
"""
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='color',
        parent_name='waterfall.decreasing.marker',
        **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop('array_ok', False),
            edit_type=kwargs.pop('edit_type', 'style'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
