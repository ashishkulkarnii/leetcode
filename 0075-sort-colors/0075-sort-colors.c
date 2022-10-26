void sortColors(int* nums, int numsSize) {
    int zero = 0, one = 0, two = 0;
    for(int i = 0; i < numsSize; ++i) {
        switch(nums[i]) {
            case 0:
                ++zero;
                break;
            case 1:
                ++one;
                break;
            case 2:
                ++two;
                break;
        }
    }
    for(int i = 0; i < numsSize; ++i) {
        if(zero > 0) {
            nums[i] = 0;
            --zero;
        }
        else if(one > 0) {
            nums[i] = 1;
            --one;
        }
        else if(two > 0) {
            nums[i] = 2;
            --two;
        }
    }
}