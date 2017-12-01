
if __name__ == "__main__":

    with open("input.txt") as f:

        lines = f.readlines()

        total_wrap_paper = 0
        total_ribbon = 0
        for i, line in enumerate(lines):

            lwh = line.strip('\n').split('x')

            if lwh[0].isdigit() and lwh[1].isdigit() and lwh[2].isdigit():
                l = int(lwh[0])
                w = int(lwh[1])
                h = int(lwh[2])

                lw = l * w
                wh = w * h
                lh = l * h

                surface_area = 2*lw + 2*wh + 2*lh
                volume = l * w * h

                # Sort dimensions
                sorted_dim = sorted([l, w, h])

                # The elves also need a little extra paper for each present:
                # the area of the smallest side.
                slack_wrap_paper = min(lw, wh, lh)
                short_dist_ribbon = 2*sorted_dim[0] + 2*sorted_dim[1]

                total_area_wrap_paper = surface_area + slack_wrap_paper
                total_width_ribbon = volume + short_dist_ribbon

                total_wrap_paper += total_area_wrap_paper
                total_ribbon += total_width_ribbon

        print '1. How many total square feet of wrapping paper should they order? %d' % total_wrap_paper
        print '2. How many total feet of ribbon should they order? %d' % total_ribbon
