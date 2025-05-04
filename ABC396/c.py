def main():
    ball_counts = [int(a) for a in input().split()]
    black_ball_count = ball_counts[0]
    white_ball_count = ball_counts[1]
    black = [int(a) for a in input().split()]
    white = [int(a) for a in input().split()]

    # 降順にソートしておく
    black.sort(reverse=True)
    white.sort(reverse=True)

    # prefix_sum 累積和
    black_prefix_sum = [0] * (black_ball_count + 1)
    white_prefix_sum = [0] * (white_ball_count + 1)
    max_white_prefix_sum = [0] * (white_ball_count + 1)

    for i in range(black_ball_count):
        black_prefix_sum[i + 1] = black_prefix_sum[i] + black[i]
    for i in range(white_ball_count):
        white_prefix_sum[i + 1] = white_prefix_sum[i] + white[i]
        max_white_prefix_sum[i + 1] = max(
            max_white_prefix_sum[i], white_prefix_sum[i + 1]
        )

    ans = 0
    for i in range(black_ball_count + 1):
        ans = max(
            ans, black_prefix_sum[i] + max_white_prefix_sum[min(i, white_ball_count)]
        )

    print(ans)


main()
