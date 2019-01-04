from pyautogui import *
from pyautogui import _failSafeCheck

def mouseMoveDragPatch(moveOrDrag, x, y, xOffset, yOffset, duration, tween=linear, button=None):
    assert moveOrDrag in ('move', 'drag'), "moveOrDrag must be in ('move', 'drag'), not %s" % (moveOrDrag)

    if sys.platform != 'darwin':
        moveOrDrag = 'move' # Only OS X needs the drag event specifically.

    xOffset = int(xOffset) if xOffset is not None else 0
    yOffset = int(yOffset) if yOffset is not None else 0

    if x is None and y is None and xOffset == 0 and yOffset == 0:
        return  # Special case for no mouse movement at all.

    startx, starty = position()

    x = int(x) if x is not None else startx
    y = int(y) if y is not None else starty

    # x, y, xOffset, yOffset are now int.
    x += xOffset
    y += yOffset

    width, height = size()

    # Make sure x and y are within the screen bounds.
    # x = max(0, min(x, width - 1))
    # y = max(0, min(y, height - 1))

    # If the duration is small enough, just move the cursor there instantly.
    steps = [(x, y)]

    if duration > MINIMUM_DURATION:
        # Non-instant moving/dragging involves tweening:
        num_steps = max(width, height)
        sleep_amount = duration / num_steps
        if sleep_amount < MINIMUM_SLEEP:
            num_steps = int(duration / MINIMUM_SLEEP)
            sleep_amount = duration / num_steps

        steps = [
            getPointOnLine(startx, starty, x, y, tween(n / num_steps))
            for n in range(num_steps)
        ]
        # Making sure the last position is the actual destination.
        steps.append((x, y))

    for tweenX, tweenY in steps:
        if len(steps) > 1:
            # A single step does not require tweening.
            time.sleep(sleep_amount)

        _failSafeCheck()
        tweenX = int(round(tweenX))
        tweenY = int(round(tweenY))
        if moveOrDrag == 'move':
            platformModule._moveTo(tweenX, tweenY)
        elif moveOrDrag == 'drag':
            platformModule._dragTo(tweenX, tweenY, button)
        else:
            raise NotImplementedError('Unknown value of moveOrDrag: {0}'.format(moveOrDrag))

    _failSafeCheck()