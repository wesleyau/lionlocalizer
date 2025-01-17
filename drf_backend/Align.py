# This class will create a list of dictionaries that contains the id, number of mismatches, author, paperurl, location id, genbanckaccession,
# indivs, locationName, lon, lat, locationType, location matchNotes, locality, accuracy
# then the output will be sorted by the least to greatest mismatches

# create a info dictionary and then create a mismatch dictionary

# or should it be a class that always runs that goes through the dictionary in the view of align
# and then dicitonary is in the parameter for this class

from .models import (
    LocHapPub,
    Sequences,
    Locations,
    Publications,
    LocHapPub,
    LHPIndividual,
)
from .serializers import (
    SequencesSerializer,
    LocationsSerializer,
    PublicationsSerializer,
    LocHapPubSerializer,
    LHPIndividualSerializer,
)
import operator


# formats output and wraps around text every 80 characters
def formattedOutput(sequence, mismatches, every=80):
    return "\n".join(
        sequence[i : i + every] + "\n" + "".join(mismatches[i : i + every])
        for i in range(0, len(sequence), every)
    )


def Align(request):
    input = request.data
    inputSeq = input["Detail"]
    seqName = ""
    seq = ""
    if inputSeq[0] == ">":  # in fasta format
        for line in inputSeq.splitlines():
            if line[0] == ">":
                seqName = line
                seq = ""
            else:
                seq = line
    else:  # not in fasta format
        seqName = ">input"  # temporary sequence id if one is not provided
        seq = inputSeq  # setting seq to the sequence
    # check for characters
    # check for length

    legitChars = "ATCG"

    # implied else
    sequenceList = []
    querySeq = seq.upper()  # alignmentQ
    seqkey = seqName  # alignmentQID
    mismatchCount = 0  # mismatch
    matchCount = 0  # match
    subjects = Sequences.objects.all()
    lionAlignment = []
    # an array that tell us whether the haplotype ID already was entered into lionAlignment
    for i in range(len(subjects)):  # len of subjects is 22
        alreadyInt = 0
        shortIndex = 0
        haplotypeID = subjects[i].id  # grabbing id of subject
        databaseSeq = subjects[i].cytB  # grabbing sequence of subject
        lions = LocHapPub.objects.filter(
            haplotype=haplotypeID
        )  # grabbing all lochappub that has subject.id

        mismatches = [
            "S",
            "u",
            "b",
            "j",
            "e",
            "c",
            "t",
            ":",
            " ",
        ]  # lazy way for adding subject to mismatches list for formatted output
        mismatchCount = 0
        matchCount = 0
        tempSeqDict = {}

        if len(querySeq) == 1140:
            # comparison for loop for 1140 bp
            for pos in range(0, len(databaseSeq)):
                # matches have . mismatches have the querySeq character
                if querySeq[pos] != databaseSeq[pos]:
                    mismatches.append(databaseSeq[pos])
                    mismatchCount += 1
                else:
                    mismatches.append(".")
                    matchCount += 1
            query = "Query:   " + querySeq  # adding query string for formatted output
            # output is every 80 characters, you can change in def formattedOutput

            formattedSeq = formattedOutput(query, mismatches)

            # if len(lions) == 0:
            #   continue # TODO: Handle the situation when a haplotype has no elephants
            locationarray = []
            lhp = []
            for l in lions:
                for indiv in LHPIndividual.objects.filter(LHP=l.location.pk):

                    lionAlignment.append(
                        {
                            "id": l.pk,
                            "haplotypeId": haplotypeID,
                            "locationID": l.location.pk,
                            "locationName": l.location.locationName,
                            "lon": l.location.lon,
                            "lat": l.location.lat,
                            "locationType": l.location.locationType,
                            "location": l.location.matchNotes,
                            "locality": l.location.locality,
                            "accuracy": l.location.accuracy,
                            "lengthOfThisArray": len(lions),
                            "mismatch": mismatchCount,
                            "match": matchCount,
                            "paperurl": l.author.paperurl,
                            "author": l.author.author,
                            "genBankAccession": indiv.genBankAccession,
                            "numLions": indiv.numLions,
                        }
                    )
        if len(querySeq) == 350:
            # comparison for loop for 350 bp
            for pos in range(430, 780):
                # matches have . mismatches have the querySeq character
                if querySeq[shortIndex] != databaseSeq[pos]:
                    mismatches.append(databaseSeq[shortIndex])
                    mismatchCount += 1
                else:
                    mismatches.append(".")
                    matchCount += 1
                shortIndex += 1
            query = "Query:   " + querySeq  # adding query string for formatted output
            # output is every 80 characters, you can change in def formattedOutput

            formattedSeq = formattedOutput(query, mismatches)

            # if len(lions) == 0:
            #   continue # TODO: Handle the situation when a haplotype has no elephants
            locationarray = []
            lhp = []
            for l in lions:
                for indiv in LHPIndividual.objects.filter(LHP=l.location.pk):

                    lionAlignment.append(
                        {
                            "id": l.pk,
                            "haplotypeId": haplotypeID,
                            "locationID": l.location.pk,
                            "locationName": l.location.locationName,
                            "lon": l.location.lon,
                            "lat": l.location.lat,
                            "locationType": l.location.locationType,
                            "location": l.location.matchNotes,
                            "locality": l.location.locality,
                            "accuracy": l.location.accuracy,
                            "lengthOfThisArray": len(lions),
                            "mismatch": mismatchCount,
                            "match": matchCount,
                            "paperurl": l.author.paperurl,
                            "author": l.author.author,
                            "genBankAccession": indiv.genBankAccession,
                            "numLions": indiv.numLions,
                        }
                    )

    res = sorted(lionAlignment, key=lambda x: x["mismatch"])

    return res
    # 36 sequences being compared to above^

    # redo data ~10 data in each table
