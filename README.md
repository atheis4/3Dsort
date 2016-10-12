# 3D Scatter Plot Animation

3D Sort will take an image file, dissect it using Pillow, and then construct a 3D scatterplot of the images pixel values using matplotlib's pyplot, Axes3D, and animation libraries.

The fully rendered scatterplot will be saved to the root file as an mp4 using ffmpeg and mencoder.

Note: Quicktime doesn't seem to natively interpret these mp4's, but they can be displayed by entering the file path in your browser.

# Setup

After cloning this repository and setting up your virtual environment, you'll need to complete the following steps to create the 3D sort and scatterplot animation:

  1. Install dependencies located in requirements.txt
  2. Download ffmpeg and mencoder using brew Install
    brew install ffmpeg
    brew install mplayer

# Usage

From [3D_anim.py](/3D_anim.py), enter the path to the image you wish to deconstruct and graph into a 3D scatter plot of pixel values as the 'source' variable on line 50.

Feel free to play with the following settings:

  1. **resize_pil_image()** (line 21):
    *Changing the width or height parameter in this function will change how many pixels are included in the final scatterplot. I recommend lower pixel values for faster processing and less visual noise. For reference, images with the max dimension set to 135px take approx 8 minutes to render.*

  2. **animate()** (line 81):
    *Changing the elev value in the view_init method will change the pitch of the plot in the final animation.*

  3. **anim** (line 100):
    *Changing the frames on line 76 will determine how many rotations your final animation will contain. My default of 720 provides two full rotations at a total time of 24 seconds.*

  4. **anim.save()** (line 104):
    *The first of the save method's parameters allows you to specify the name, path, and file type of the output. Check out the ffmpeg or mencoder docs to see which file types are supported.*

Run program from command line and enjoy!
