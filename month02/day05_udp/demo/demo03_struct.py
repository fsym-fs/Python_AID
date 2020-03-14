import struct

# 数据：1 b"Lily" 168 92.5
# 确定格式对象
st = struct.Struct("i4sif")
# 数据打包
data = st.pack(1, b'Lily', 168, 92.5)
print(data)
# 数据解包
print(st.unpack(data))
