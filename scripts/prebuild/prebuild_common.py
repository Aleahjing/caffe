variant_types  = ['bool', 'char', 'int8_t', 'int16_t', 'int32_t', 'int64_t',
                  'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t', 'half_fp',
                  'float', 'double']

pointer_variant_types = variant_types + ['void']

variant_enable_flags = dict()

variant_enable_flags['int8_t'] = 'USE_INT_QUANT_8'
variant_enable_flags['int16_t'] = 'USE_INT_QUANT_16'
variant_enable_flags['int32_t'] = 'USE_INT_QUANT_32'
variant_enable_flags['int64_t'] = 'USE_INT_QUANT_64'
variant_enable_flags['uint8_t'] = 'USE_INT_QUANT_8'
variant_enable_flags['uint16_t'] = 'USE_INT_QUANT_16'
variant_enable_flags['uint32_t'] = 'USE_INT_QUANT_32'
variant_enable_flags['uint64_t'] = 'USE_INT_QUANT_64'
variant_enable_flags['half_fp'] = 'USE_HALF'
variant_enable_flags['float'] = 'USE_SINGLE'
variant_enable_flags['double'] = 'USE_DOUBLE'

proto_types = dict()

proto_types['half_fp'] = 'HALF'
proto_types['float'] = 'FLOAT'
proto_types['double'] = 'DOUBLE'
proto_types['int8_t'] = 'INT8_QUANTIZED'
proto_types['int16_t'] = 'INT16_QUANTIZED'
proto_types['int32_t'] = 'INT32_QUANTIZED'
proto_types['int64_t'] = 'INT64_QUANTIZED'
#proto_types[''] = 'PACKED_BINARY'