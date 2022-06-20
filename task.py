current_channels = [2, 3, 4, 5]
channel_groups = [[1, 2, 3, 4], [2, 3, 5, 4], [4, 3, 6], [8, 3, 7, 5], [6, 10, 8, 9, 7]]
bad_channel = 7
answer = []
all_channels = []

for group in channel_groups:
    if bad_channel not in group and len(group) <= len(current_channels):
        answer += [group]

    for key in group:
        if key not in all_channels:
            all_channels += [key]

if answer:
    answer = max(answer)
else:
    answer = 999999
    for channel in all_channels:
        for i in range(1, max(all_channels) + 1):
            if channel == bad_channel + i and channel + i < answer:
                answer = channel

print(answer)
