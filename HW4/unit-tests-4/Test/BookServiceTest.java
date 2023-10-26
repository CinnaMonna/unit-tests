import org.mockito.Mockito;
import seminars.fourth.book.BookRepository;

import static org.mockito.Mockito.*;



public class BookServiceTest {
    //Arrange
    BookRepository repositoryMock = mock(BookRepository.class);
    Mockito.when(repositoryMock.findById(String id)).then
    when(repositoryMock.findById((String id))).thenReturn(bookRepository.findById(id););
}

