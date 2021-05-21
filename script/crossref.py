import requests
import json


def crossrefGet(doi):
    """
    Get the metadata offered by crossref.org
    :param doi: text string of the doi number
    :return: metadata by crossref api
    """
    crossrefapi = "https://api.crossref.org/v1/works/{}"
    metadata = requests.get(crossrefapi.format(doi))
    metadata = json.loads(metadata.content)
    if metadata["status"] == "ok":
        return metadata
    else:
        raise RuntimeError("Do not get proper metadata")


def crossrefMetadataToCSL(metadata):
    """
    Convert the metadata got by crossref api into csl-friendly format
    the format is referred in https://www.crossref.org/labs/citation-formatting-service/
    Need to integrate the CSL(https://citationstyles.org/developers/) style
    Need a smarter way to handle those keys not exists or duplicated

    :param metadata:
    :return: csl-friendly format as dict
    """
    content = metadata["message"]
    return {
            "volume": content["volume"],
            "issue": content["issue"],
            "DOI": content["DOI"],
            "title": content["title"],
            "container-title": content["container-title"],
            "issued": content["issued"],
            "author": content["author"],
            "page": content["page"] if "page" in content.keys() else content["article-number"],
            "type": content["type"]
    }


def crossrefMetadataParser(metadata, filename):
    """
    Return the metadata of the paper with the bibtex entry format

    :param metadata: metadata by crossref api
    :param filename: the path to store the bibtex entry
    :return: None
    """
    bibtexFormat = (
        ""
    )



if __name__ == "__main__":
    testdoi = "10.1109/5.771073"
    crossrefapi = "https://api.crossref.org/v1/works/{}"

    metadata = crossrefGet(testdoi)

    print(crossrefMetadataToCSL(metadata))
