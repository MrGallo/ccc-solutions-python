num_streams = int(input())
stream_flows = []
for i in range(num_streams):
    stream_flows.append(int(input()))

while True:
    input_num = int(input())
    if input_num == 77:
        break
    elif input_num == 99:
        stream_num = int(input())-1
        stream_flow_percent = int(input())/100
        left_flow_value = stream_flows[stream_num] * stream_flow_percent
        right_flow_value = stream_flows[stream_num] * (1-stream_flow_percent)
        stream_flows = (stream_flows[:stream_num] +
                        [left_flow_value, right_flow_value] +
                        stream_flows[stream_num+1:])
    elif input_num == 88:
        stream_num = int(input())-1
        left_flow_value = stream_flows[stream_num] + stream_flows[stream_num+1]
        stream_flows = (stream_flows[:stream_num] + 
                        [left_flow_value] +
                        stream_flows[stream_num+2:])

print(*[round(n) for n in stream_flows])
