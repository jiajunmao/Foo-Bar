def answer(m):
    print(back_track(m, m, 0, [], [], 0))


def back_track(total_bricks, bricks_left, current_height, current_track, visited, times):
    #print(current_track)
    if len(current_track) != 0:
        if current_track[0] == total_bricks:
            return times


    elif sum_array(current_track) == total_bricks and bricks_left==0:
        return back_track(
            total_bricks=total_bricks,
            bricks_left=total_bricks,
            current_height=1,
            current_track=current_track[:len(current_track)-1],
            visited=[],
            times=times+1
        )

    elif bricks_left < current_height:
        return back_track(
            total_bricks=total_bricks,
            bricks_left=bricks_left+current_track[len(current_track)-1],
            current_height=current_track[len(current_track)-2],
            current_track=current_track[:len(current_track)],
            visited=visited[:len(visited)],
            times=times
        )

    else:
        #print(current_height+1)
        current_track.append(current_height+1)
        visited.append(current_height+1)

        return back_track(
            total_bricks=total_bricks,
            bricks_left=bricks_left-current_height-1,
            current_height=current_height+1,
            current_track=current_track,
            visited=visited,
            times=times
        )


def sum_array(array):
    total = 0
    for element in array:
        total = total+element
    return total


def main():
    answer(3)


if __name__ == "__main__":
    main()