# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa: F401
from jax._src.lax.lax import (
  ConvDimensionNumbers as ConvDimensionNumbers,
  ConvGeneralDilatedDimensionNumbers as ConvGeneralDilatedDimensionNumbers,
  DotDimensionNumbers as DotDimensionNumbers,
  GatherDimensionNumbers as GatherDimensionNumbers,
  GatherScatterMode as GatherScatterMode,
  Precision as Precision,
  RandomAlgorithm as RandomAlgorithm,
  RoundingMethod as RoundingMethod,
  ScatterDimensionNumbers as ScatterDimensionNumbers,
  abs as abs,
  abs_p as abs_p,
  acos as acos,
  acos_p as acos_p,
  acosh as acosh,
  acosh_p as acosh_p,
  abs as abs,
  abs_p as abs_p,
  acos as acos,
  acosh as acosh,
  acosh_p as acosh_p,
  add as add,
  add_p as add_p,
  after_all as after_all,
  after_all_p as after_all_p,
  and_p as and_p,
  argmax as argmax,
  argmax_p as argmax_p,
  argmin as argmin,
  argmin_p as argmin_p,
  asin as asin,
  asin_p as asin_p,
  asinh as asinh,
  asinh_p as asinh_p,
  atan as atan,
  atan_p as atan_p,
  atan2 as atan2,
  atan2_p as atan2_p,
  atanh as atanh,
  atanh_p as atanh_p,
  batch_matmul as batch_matmul,
  bessel_i0e as bessel_i0e,
  bessel_i0e_p as bessel_i0e_p,
  bessel_i1e as bessel_i1e,
  bessel_i1e_p as bessel_i1e_p,
  betainc as betainc,
  bitcast_convert_type as bitcast_convert_type,
  bitcast_convert_type_p as bitcast_convert_type_p,
  bitwise_and as bitwise_and,
  bitwise_not as bitwise_not,
  bitwise_or as bitwise_or,
  bitwise_xor as bitwise_xor,
  broadcast as broadcast,
  broadcast_in_dim as broadcast_in_dim,
  broadcast_in_dim_p as broadcast_in_dim_p,
  broadcast_shapes as broadcast_shapes,
  broadcast_to_rank as broadcast_to_rank,
  broadcasted_iota as broadcasted_iota,
  cbrt as cbrt,
  cbrt_p as cbrt_p,
  ceil as ceil,
  ceil_p as ceil_p,
  clamp as clamp,
  clamp_p as clamp_p,
  clz as clz,
  clz_p as clz_p,
  collapse as collapse,
  complex as complex,
  complex_p as complex_p,
  concatenate as concatenate,
  concatenate_p as concatenate_p,
  conj as conj,
  conj_p as conj_p,
  conv as conv,
  conv_dimension_numbers as conv_dimension_numbers,
  conv_general_dilated as conv_general_dilated,
  conv_general_dilated_p as conv_general_dilated_p,
  conv_general_permutations as conv_general_permutations,
  conv_general_shape_tuple as conv_general_shape_tuple,
  conv_shape_tuple as conv_shape_tuple,
  conv_transpose as conv_transpose,
  conv_transpose_shape_tuple as conv_transpose_shape_tuple,
  conv_with_general_padding as conv_with_general_padding,
  convert_element_type as convert_element_type,
  _convert_element_type as _convert_element_type,
  convert_element_type_p as convert_element_type_p,
  cos as cos,
  cos_p as cos_p,
  cosh as cosh,
  cosh_p as cosh_p,
  create_token as create_token,
  create_token_p as create_token_p,
  digamma as digamma,
  digamma_p as digamma_p,
  div as div,
  div_p as div_p,
  dot as dot,
  dot_general as dot_general,
  dot_general_p as dot_general_p,
  dtype as dtype,
  dtypes as dtypes,
  dynamic_index_in_dim as dynamic_index_in_dim,
  dynamic_slice as dynamic_slice,
  dynamic_slice_in_dim as dynamic_slice_in_dim,
  dynamic_slice_p as dynamic_slice_p,
  dynamic_update_index_in_dim as dynamic_update_index_in_dim,
  dynamic_update_slice as dynamic_update_slice,
  dynamic_update_slice_in_dim as dynamic_update_slice_in_dim,
  dynamic_update_slice_p as dynamic_update_slice_p,
  eq as eq,
  eq_p as eq_p,
  erf as erf,
  erf_inv as erf_inv,
  erf_inv_p as erf_inv_p,
  erf_p as erf_p,
  erfc as erfc,
  erfc_p as erfc_p,
  exp as exp,
  exp_p as exp_p,
  expand_dims as expand_dims,
  expm1 as expm1,
  expm1_p as expm1_p,
  floor as floor,
  floor_p as floor_p,
  full as full,
  full_like as full_like,
  gather as gather,
  gather_p as gather_p,
  ge as ge,
  ge_p as ge_p,
  gt as gt,
  gt_p as gt_p,
  igamma as igamma,
  igamma_grad_a as igamma_grad_a,
  igamma_grad_a_p as igamma_grad_a_p,
  igamma_p as igamma_p,
  igammac as igammac,
  igammac_p as igammac_p,
  imag as imag,
  imag_p as imag_p,
  index_in_dim as index_in_dim,
  index_take as index_take,
  infeed as infeed,
  infeed_p as infeed_p,
  integer_pow as integer_pow,
  integer_pow_p as integer_pow_p,
  iota as iota,
  iota_p as iota_p,
  is_finite as is_finite,
  is_finite_p as is_finite_p,
  itertools as itertools,
  le as le,
  le_p as le_p,
  lgamma as lgamma,
  lgamma_p as lgamma_p,
  log as log,
  log1p as log1p,
  log1p_p as log1p_p,
  log_p as log_p,
  lt as lt,
  lt_p as lt_p,
  max as max,
  max_p as max_p,
  min as min,
  min_p as min_p,
  mul as mul,
  mul_p as mul_p,
  naryop as naryop,
  naryop_dtype_rule as naryop_dtype_rule,
  ne as ne,
  ne_p as ne_p,
  neg as neg,
  neg_p as neg_p,
  nextafter as nextafter,
  nextafter_p as nextafter_p,
  not_p as not_p,
  or_p as or_p,
  outfeed as outfeed,
  outfeed_p as outfeed_p,
  pad as pad,
  pad_p as pad_p,
  padtype_to_pads as padtype_to_pads,
  population_count as population_count,
  population_count_p as population_count_p,
  pow as pow,
  pow_p as pow_p,
  prod as prod,
  random_gamma_grad as random_gamma_grad,
  random_gamma_grad_p as random_gamma_grad_p,
  real as real,
  real_p as real_p,
  reciprocal as reciprocal,
  reduce as reduce,
  reduce_and_p as reduce_and_p,
  reduce_max_p as reduce_max_p,
  reduce_min_p as reduce_min_p,
  reduce_or_p as reduce_or_p,
  reduce_p as reduce_p,
  reduce_precision as reduce_precision,
  reduce_precision_p as reduce_precision_p,
  reduce_prod_p as reduce_prod_p,
  reduce_sum_p as reduce_sum_p,
  regularized_incomplete_beta_p as regularized_incomplete_beta_p,
  rem as rem,
  rem_p as rem_p,
  reshape as reshape,
  reshape_p as reshape_p,
  rev as rev,
  rev_p as rev_p,
  rng_bit_generator as rng_bit_generator,
  rng_bit_generator_p as rng_bit_generator_p,
  rng_uniform as rng_uniform,
  rng_uniform_p as rng_uniform_p,
  round as round,
  round_p as round_p,
  rsqrt as rsqrt,
  rsqrt_p as rsqrt_p,
  scatter as scatter,
  scatter_add as scatter_add,
  scatter_add_p as scatter_add_p,
  scatter_max as scatter_max,
  scatter_max_p as scatter_max_p,
  scatter_min as scatter_min,
  scatter_min_p as scatter_min_p,
  scatter_mul as scatter_mul,
  scatter_mul_p as scatter_mul_p,
  scatter_p as scatter_p,
  select as select,
  select_p as select_p,
  shift_left as shift_left,
  shift_left_p as shift_left_p,
  shift_right_arithmetic as shift_right_arithmetic,
  shift_right_arithmetic_p as shift_right_arithmetic_p,
  shift_right_logical as shift_right_logical,
  shift_right_logical_p as shift_right_logical_p,
  sign as sign,
  sign_p as sign_p,
  sin as sin,
  sin_p as sin_p,
  sinh as sinh,
  sinh_p as sinh_p,
  slice as slice,
  slice_in_dim as slice_in_dim,
  slice_p as slice_p,
  sort as sort,
  sort_key_val as sort_key_val,
  sort_p as sort_p,
  sqrt as sqrt,
  sqrt_p as sqrt_p,
  square as square,
  squeeze as squeeze,
  squeeze_p as squeeze_p,
  standard_abstract_eval as standard_abstract_eval,
  standard_naryop as standard_naryop,
  standard_primitive as standard_primitive,
  standard_unop as standard_unop,
  stop_gradient as stop_gradient,
  sub as sub,
  sub_p as sub_p,
  tan as tan,
  tan_p as tan_p,
  tanh as tanh,
  tanh_p as tanh_p,
  tie_in as tie_in,
  top_k as top_k,
  top_k_p as top_k_p,
  transpose as transpose,
  transpose_p as transpose_p,
  unop as unop,
  unop_dtype_rule as unop_dtype_rule,
  xor_p as xor_p,
  zeros_like_array as zeros_like_array,
)
from jax._src.lax.lax import (
  _reduce_sum, _reduce_max, _reduce_min, _reduce_or, _reduce_and,
  _float, _complex, _input_dtype,
  _const, _eq_meet, _broadcasting_select,
  _check_user_dtype_supported, _one, _zero,
  _upcast_fp16_for_computation, _broadcasting_shape_rule,
  _eye, _tri, _delta, _ones, _zeros, _dilate_shape)
from jax._src.lax.windowed_reductions import (
  _reduce_window_sum,
  _reduce_window_max,
  _reduce_window_min,
  _reduce_window_prod,
  _select_and_gather_add,
  _select_and_scatter_add,
  reduce_window as reduce_window,
  reduce_window_max_p as reduce_window_max_p,
  reduce_window_min_p as reduce_window_min_p,
  reduce_window_p as reduce_window_p,
  reduce_window_shape_tuple as reduce_window_shape_tuple,
  reduce_window_sum_p as reduce_window_sum_p,
  select_and_gather_add_p as select_and_gather_add_p,
  select_and_scatter_p as select_and_scatter_p,
  select_and_scatter_add_p as select_and_scatter_add_p,
)
from jax._src.lax.control_flow import (
  associative_scan as associative_scan,
  cond as cond,
  cond_p as cond_p,
  cummax as cummax,
  cummax_p as cummax_p,
  cummin as cummin,
  cummin_p as cummin_p,
  cumprod as cumprod,
  cumprod_p as cumprod_p,
  cumsum as cumsum,
  cumsum_p as cumsum_p,
  custom_linear_solve as custom_linear_solve,
  custom_root as custom_root,
  fori_loop as fori_loop,
  linear_solve_p as linear_solve_p,
  map as map,
  scan as scan,
  scan_bind as scan_bind,
  scan_p as scan_p,
  switch as switch,
  while_loop as while_loop,
  while_p as while_p,
)
from jax._src.lax.fft import (
  fft as fft,
  fft_p as fft_p,
)
from jax._src.lax.parallel import (
  all_gather as all_gather,
  all_to_all as all_to_all,
  all_to_all_p as all_to_all_p,
  axis_index as axis_index,
  axis_index_p as axis_index_p,
  pmax as pmax,
  pmax_p as pmax_p,
  pmean as pmean,
  pmin as pmin,
  pmin_p as pmin_p,
  ppermute as ppermute,
  ppermute_p as ppermute_p,
  pshuffle as pshuffle,
  psum as psum,
  psum_p as psum_p,
  psum_scatter as psum_scatter,
  pswapaxes as pswapaxes,
  pdot as pdot,
  xeinsum as xeinsum,
)
from jax._src.lax.other import (
  conv_general_dilated_patches as conv_general_dilated_patches
)
from jax._src.ad_util import stop_gradient_p as stop_gradient_p
from . import linalg as linalg
