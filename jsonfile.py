import json
from collections import defaultdict
import matplotlib.pyplot as plt

def total_number_images(data):
    """
    This function counts the total number of images in the dataset JSON annotation data
    :param data: is the dataset, the Json variable containing all the annotations for each image of the dataset
    :return: Total number of images in the dataset
    """
    numberImage= len(data['images'])
    return numberImage

def annotations_per_categories(data):
    """
    This function counts and return for each pathology (category) the number of annotations having this pathology
    :param data: is the dataset, the Json variable containing all the annotations for each image of the dataset
    :return: Pathology/Category ID, Category Name (pathology name) and Number of Annotations
    """
    for annotation_elt in data['annotations']: # for each annotation
        category_id = annotation_elt['category_id'] # get the id of the annotation
        annotations_per_category[category_id] += 1 # add 1 to the number of annotations if the category is category_id

    # Print the number of annotations per category
    for category_id, count in annotations_per_category.items():
        print(f'Category ID {category_id}: {classNames[category_id]}: {count} annotations')


def histogram_annotation_per_category(annotations_per_category):
    """
    This function draw the histogram of number of annotations per pathology.
    On the x-axis we have the pathology name and on the y-axis we have the number of annotations
    :param annotations_per_category:
    :return: A histogram
    """
    # Get the category IDs and counts for plotting
    category_ids = list(annotations_per_category.keys())
    the_classes=[]
    for id in category_ids:
        the_classes.append(classNames[id])
    #print("category_ids=",category_ids)
    #print("class=", the_classes)
    counts = list(annotations_per_category.values())

    # Plot histogram
    plt.figure(figsize=(20, 6))
    plt.bar(the_classes, counts)
    plt.xlabel('Classes/Pathologies')
    plt.ylabel('Number of Annotations')
    plt.title('Number of Annotations per Category')
    plt.show()


def Images_per_category(categortID,data):
    """
    This function returns the list of the images containing the
    pathology of a given class categortID
    :param categortID: is an interger for the pathology class.
    In our case categortID is from 0 to 7 as we have 8 pathology classes in the dataset
    :param data: is the dataset, the Json variable containing all the annotations for each image of the dataset

    :return: listImages which is a list of the images containing the pathology
    """
    images=data['images']
    # Create the dictionary and map category IDs to category names
    image_id_to_category_id = [{'category_id': annotation['category_id'], 'image_id': annotation['image_id']}
                                        for annotation in data['annotations']]

    # Find the images IDs for the given category ID
    image_ids = [entry['image_id'] for entry in image_id_to_category_id if entry['category_id'] == categortID]
    listImages=[]  # the list of images we are searching for
    for elt in images:
        elt_id=elt['id']
        if elt_id in image_ids:
            listImages.append(elt['file_name'])
    return listImages


# Open and read the pathology annotation JSON file and put it into variable data
#
with open('coco_training.json', 'r') as f:
    data = json.load(f)


annotations_per_category = defaultdict(int)  # Initialize a dictionary to count annotations per category
classNames = ["Angiectasia", "Blood-fresh", "Erosion", "Erythema", "Foreign-Body", "Lymphangiectasia", "Polyp",
              "Ulcer"]  # class names (pathologies names)

# Print the total number of images
print("Number of image:",total_number_images(data),"\n")

annotations_per_categories(data) # get annotation per category and print
histogram_annotation_per_category(annotations_per_category) # Draw the histogram for annotation per pathology
print(Images_per_category(1,data)) # Print list of images having the annotation of a pathology with ID=1.
print("\n Size:",len(Images_per_category(1,data)),"\n")