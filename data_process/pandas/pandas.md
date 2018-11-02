
## DataFrame 属性
    T	Transpose index and columns.
    at	Access a single value for a row/column label pair.
    axes	Return a list representing the axes of the DataFrame.
    blocks	(DEPRECATED) Internal property, property synonym for as_blocks()
    columns	The column labels of the DataFrame.
    dtypes	Return the dtypes in the DataFrame.
    empty	Indicator whether DataFrame is empty.
    ftypes	Return the ftypes (indication of sparse/dense and dtype) in DataFrame.
    iat	Access a single value for a row/column pair by integer position.
    iloc	Purely integer-location based indexing for selection by position.
    index	The index (row labels) of the DataFrame.
    ix	A primarily label-location based indexer, with integer position fallback.
    loc	Access a group of rows and columns by label(s) or a boolean array.
    ndim	Return an int representing the number of axes / array dimensions.
    shape	Return a tuple representing the dimensionality of the DataFrame.
    size	Return an int representing the number of elements in this object.
    style	Property returning a Styler object containing methods for building a styled HTML representation fo the DataFrame.
    values	Return a Numpy representation of the DataFrame.
    
   
### pandas.DataFrame.filter
    DataFrame.filter(items=None, like=None, regex=None, axis=None)
#### 参数说明    
    items : list-like
            List of info axis to restrict to (must not all be present)
    like : string
            Keep info axis where “arg in col == True”
    regex : string (regular expression)
            Keep info axis with re.search(regex, col) == True
    axis : int or string axis name
            The axis to filter on. By default this is the info axis, ‘index’ for Series, ‘columns’ for DataFrame
    
    Returns: same type as input object
    
    
### pandas.DataFrame.fillna
    DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
#### 参数说明


### pandas.DataFrame.append
    DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=None)

#### 参数说明


### pandas.DataFrame.apply
    DataFrame.apply(func, axis=0, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds)

#### 参数说明


### pandas.DataFrame.applymap
    DataFrame.applymap(func)[source]

#### 参数说明


### pandas.DataFrame.drop
    DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

#### 参数说明


### pandas.DataFrame.drop_duplicates
    DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
#### 参数说明


### pandas.DataFrame.reindex
    DataFrame.reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=True, level=None, fill_value=nan, limit=None, tolerance=None)
#### 参数说明


### pandas.DataFrame.rename
    DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None)
#### 参数说明


### pandas.DataFrame.resample
    DataFrame.resample(rule, how=None, axis=0, fill_method=None, closed=None, label=None, convention='start', kind=None, loffset=None, limit=None, base=0, on=None, level=None)


### pandas.DataFrame.replace
    DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad')
    

### pandas.DataFrame.reset_index
    DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
    
### pandas.DataFrame.update
    DataFrame.update(other, join='left', overwrite=True, filter_func=None, raise_conflict=False)