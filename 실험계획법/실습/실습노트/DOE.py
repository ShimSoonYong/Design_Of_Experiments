# DOE Class Module

from pandas import DataFrame

def effect_est(data:DataFrame, sign_col:list, value_cols:list)->float:
    """
    # Factor Effect Estimator for DOE Class.

    Args:
        data (pd.DataFrame): Wide-Format pandas dataframe with design matrix, and real number data.
        sign_col (list): A list of strings in design matrix in "`data`".
        value_cols (list): A list of strings real number data.

    Returns:
        Factor_Effect (pd.DataFrame): `(data[sign_col] * data[value_cols].sum(1)).mean()`

    Example:
            ```
            import pandas as pd
            df = pd.DataFrame({
                'a': [-1, 1, -1, 1, -1, 1, -1, 1],
                'b': [-1, -1, 1, 1, -1, -1, 1, 1],
                'c': [-1,-1,-1,-1, 1, 1, 1, 1],
                '처리조합': ['(1)', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc'],
                'I': [22, 32, 35, 55, 44, 40, 60, 39],
                'II': [31, 43, 34, 47, 45, 37, 50, 41],
                'III': [25, 29, 50, 46, 38, 36, 54, 47]
            })
            from DOE import effect_est

            for fac in df['처리조합']:
                if fac == '(1)':
                    continue
                print(f'요인 {fac}의 효과:', effect_est(data=df, sign_col=[f for f in fac], value_cols=['I','II', 'III']))
            ```
            >>> 요인 a의 효과: 0.5
            >>> 요인 b의 효과: 17.0
            >>> 요인 ab의 효과: -2.5
            >>> 요인 c의 효과: 10.25
            >>> 요인 ac의 효과: -13.25
            >>> 요인 bc의 효과: -4.25
            >>> 요인 abc의 효과: -3.25

    """
    return (data[sign_col].prod(1) * data[value_cols].mean(1)).mean()*2
        
if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame({
        'a': [-1, 1, -1, 1, -1, 1, -1, 1],
        'b': [-1, -1, 1, 1, -1, -1, 1, 1],
        'c': [-1,-1,-1,-1, 1, 1, 1, 1],
        '처리조합': ['(1)', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc'],
        'I': [22, 32, 35, 55, 44, 40, 60, 39],
        'II': [31, 43, 34, 47, 45, 37, 50, 41],
        'III': [25, 29, 50, 46, 38, 36, 54, 47]
        })

    for fac in df['처리조합']:
        if fac == '(1)':
            continue
        print(f'요인 {fac}의 효과:', effect_est(data=df, sign_col=[f for f in fac], value_cols=['I','II', 'III']))