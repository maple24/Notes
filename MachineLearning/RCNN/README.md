## Region Proposal Network (RPN)
1. region proposal: Given an input image find all possible places where objects can be located.

The output of this stage should be a list of bounding boxes of likely positions of objects.

These are often called region proposals or regions of interest.

1. find classification: For every region proposal from the previous stage, decide whether it belongs to one of the target classes or to the background. Here we could use a deep convolution network.                                                                  